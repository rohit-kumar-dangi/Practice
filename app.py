from flask import Flask, render_template, request, redirect, session,flash
from flask_mysqldb import MySQL
from datetime import datetime, timedelta
import threading
import time

app = Flask(__name__)
app.secret_key = "secret123"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rohit'
app.config['MYSQL_DB'] = 'smart_attendance'

# app.config['MYSQL_HOST'] = 'trolley.proxy.rlwy.net'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'RhLuUwTrcyCGfQumZBinZmiOTNbbamVo'
# app.config['MYSQL_DB'] = 'smart_attendance'
# app.config['MYSQL_PORT'] = 30821

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

#teacher section
@app.route("/teacher_login", methods=["GET","POST"])
def teacher_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM teachers WHERE email=%s AND password=%s",(email, password))
        teacher = cur.fetchone()

        if teacher:
            session["teacher"] = {
                "id" : teacher[0],
                "name" : teacher[1],
                "email": teacher[2],
                "role" : teacher[4],
                "departmant" : teacher[5]
            }
            return redirect("/teacher_dashboard")
        else:
            flash("Invalid Email or Password")
            return redirect("/teacher_login")
    return render_template("teacher_login.html")


@app.route("/teacher_dashboard")
def teacher_dashboard():
    if "teacher" in session:
        return render_template("teacher_dashboard.html")
    else:
        return redirect("/teacher_login")
    
@app.route("/take_attendance")
def take_attendance():

    if "teacher" not in session:
        return redirect("/teacher_login")

    cur = mysql.connection.cursor()

    cur.execute("SELECT department_id, department FROM departments")
    departments = cur.fetchall()

    cur.execute("SELECT DISTINCT semester FROM subjects ORDER BY semester")
    semesters = cur.fetchall()

    cur.execute("SELECT subject_id, subject_name FROM subjects")
    subjects = cur.fetchall()

    return render_template("take_attendance.html",teacher=session["teacher"],departments=departments,semesters=semesters,subjects=subjects)

@app.route("/start_session", methods=["POST"])
def start_session():

    if "teacher" not in session:
        return redirect("/teacher_login")

    department_id = request.form["department"]
    semester = request.form["semester"]
    subject_id = request.form["subject"]
    minutes = int(request.form["qr_valid_minutes"])

    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=minutes)

    cur = mysql.connection.cursor()

    # Close any previous active session(for testing)
    cur.execute("UPDATE attendance_sessions SET status='CLOSED' WHERE status='OPEN'")

    # Create new attendance session
    cur.execute("INSERT INTO attendance_sessions(department_id, semester, subject_id, start_time, end_time, status)VALUES (%s,%s,%s,%s,%s,'OPEN')",(department_id, semester, subject_id, start_time, end_time))

    mysql.connection.commit()
    session_id = cur.lastrowid
    cur.close()

    # Start background thread (runs once)
    thread = threading.Thread(
        target=close_session_after_delay,
        args=(session_id, minutes)
    )
    thread.start()
    flash("Attendance session started successfully !")

    return redirect("/take_attendance")


def close_session_after_delay(session_id, minutes):
    time.sleep(minutes * 60)

    # give Flask app context to thread
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE attendance_sessions SET status='CLOSED' WHERE id=%s", (session_id,))
        mysql.connection.commit()
        cur.close()

        print("Session closed automatically:", session_id)

@app.route("/register_face")
def register_face():
    if "teacher" not in session:
        return redirect("/teacher_login")
    
    cur = mysql.connection.cursor()

    cur.execute("SELECT department_id, department FROM departments")
    departments = cur.fetchall()
    cur.execute("SELECT DISTINCT course FROM subjects ORDER BY course")
    courses = cur.fetchall()
    cur.execute("SELECT DISTINCT semester FROM subjects ORDER BY semester")
    semesters = cur.fetchall()
    cur.execute("SELECT student_id,name FROM students ORDER BY student_id")
    students=cur.fetchall()
    cur.close()
    return render_template("register_face.html",teacher=session["teacher"],departments=departments,courses=courses,semesters=semesters,students=students)

@app.route("/add_face", methods=["POST"])
def add_face():

    if "teacher" not in session:
        return "Login required"

    student_id = request.form["student"]

    if "image" not in request.files:
        return "No image received"

    image = request.files["image"]

    import face_recognition
    import numpy as np
    import json

    img = face_recognition.load_image_file(image)
    encodings = face_recognition.face_encodings(img)

    if not encodings:
        return "No face detected"

    encoding = encodings[0].tolist()

    cur = mysql.connection.cursor()

    cur.execute(
        "UPDATE students SET face_encoding=%s WHERE student_id=%s",
        (json.dumps(encoding), student_id)
    )

    mysql.connection.commit()

    return "Face registered successfully"

@app.route("/logout_teacher")
def logout_teacher():
    session.pop("teacher", None)
    return redirect("/")



#student section
@app.route("/student_login", methods=["GET","POST"])
def student_login():
    if request.method=="POST":
        roll=request.form["username"]
        password=request.form["password"]

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE roll=%s AND password=%s",(roll,password))
        student=cur.fetchone()
        if student:
            session["student"]={
                "id" : student[0],
                "roll" : student[1],
                "name": student[2],
                "department" : student[4],
                "semester" : student[5],
                "course" : student[6]
            }
            return redirect("/student_dashboard")
        else:
            flash("Invalid Email or Password")
            return redirect("/student_login")
    return render_template("student_login.html")


@app.route("/student_dashboard")
def student_dashboard():
    if "student" in session:
        s_id=session["student"]["id"]
        return render_template("student_dashboard.html",student=session["student"])
    else:
        return redirect("/student_login")

@app.route("/mark_attendance")
def mark_attendance():

    if "student" not in session:
        return redirect("/student_login")

    student_id = session["student"]["id"]
    student_dept = session["student"]["department"]
    student_sem = session["student"]["semester"]
    
    print(student_dept,student_sem)
    cur = mysql.connection.cursor()

    # get latest OPEN attendance session
    cur.execute("SELECT id FROM attendance_sessions WHERE status='OPEN' AND department_id=%s AND semester=%s ORDER BY id DESC LIMIT 1", (student_dept, student_sem))
    active_session = cur.fetchone()

    # if no session running
    if not active_session:
        return render_template("mark_attendance.html",student=session["student"],session_open=False)

    session_id = active_session[0]

    # already marked or not
    cur.execute("SELECT * FROM attendance_records WHERE session_id=%s AND student_id=%s", (session_id, student_id))

    if cur.fetchone():
        return render_template("mark_attendance.html",student=session["student"],session_open=True,already_marked=True)
    
    return render_template("mark_attendance.html",student=session["student"],session_open=True,already_marked=False)

@app.route("/mark_present")
def mark_present():

    if "student" not in session:
        return redirect("/student_login")

    student_id = session["student"]["id"]
    student_dept = session["student"]["department"]
    student_sem = session["student"]["semester"]
    cur = mysql.connection.cursor()

    # get active session matching student
    cur.execute("SELECT id FROM attendance_sessions WHERE status='OPEN' AND department_id=%s AND semester=%s ORDER BY id DESC LIMIT 1", (student_dept, student_sem))


    session_data = cur.fetchone()

    if not session_data:
        flash("Attendance session closed")
        return redirect("/mark_attendance")

    session_id = session_data[0]

    cur.execute("INSERT INTO attendance_records (session_id, student_id, attend, marked_time) VALUES (%s,%s,'Present',NOW())", (session_id, student_id))

    mysql.connection.commit()
    flash("Attendance Marked Successfully")

    return render_template("mark_attendance.html",student=session["student"],session_open=True,already_marked=True)



@app.route("/verify_face", methods=["POST"])
def verify_face():

    if "student" not in session:
        return "Login required"

    if "image" not in request.files:
        return "No image received"

    image = request.files["image"]

    import face_recognition
    import numpy as np
    import json

    img = face_recognition.load_image_file(image)

    encodings = face_recognition.face_encodings(img)

    if not encodings:
        return "No face detected"

    captured = encodings[0]

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT face_encoding FROM students WHERE student_id=%s",
        (session["student"]["id"],)
    )

    data = cur.fetchone()

    if not data or not data[0]:
        return "Face not registered"

    stored = np.array(json.loads(data[0]))

    match = face_recognition.compare_faces([stored], captured)

    if match[0]:
        return "Face Verified"
    else:
        return "Face not matched"

@app.route("/logout_student")
def logout_student():
    session.pop("student", None)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    # app.run(host="0.0.0.0", port=5000)
    #app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")