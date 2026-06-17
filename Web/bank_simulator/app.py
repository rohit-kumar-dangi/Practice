from flask import Flask, render_template, request, redirect,url_for , session, flash, Response
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv
import csv
import random

app=Flask(__name__)
app.secret_key = "Rohit_bank_sim"

app.config['MYSQL_HOST'] = os.environ.get("DB_HOST")
app.config['MYSQL_USER'] = os.environ.get("DB_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("DB_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("DB_NAME")

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        mobile = request.form["mobile"]
        email = request.form["email"]
        aadhaar = request.form["aadhaar"]
        pan = request.form["pan"]
        address = request.form["address"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO users (name, mobile, email, aadhaar, pan, address, password)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (name,mobile,email,aadhaar,pan,address,password))

        mysql.connection.commit()
        flash("User registration successfully")
        return redirect(url_for("index"))

    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login():
    userid=request.form["userid"]
    password=request.form["password"]

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE user_id=%s AND password=%s",(userid,password))
    user=cur.fetchone()

    if user:
        session["user"]={"userid": user[0]}
        return redirect(url_for("dashboard"))
    else:
        flash("Invalid Email or Password")
        return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    user_id = session["user"]["userid"]

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM accounts WHERE user_id=%s",(user_id,))
    accounts = cur.fetchall()

    return render_template("dashboard.html", accounts=accounts)

@app.route("/deposit", methods=["GET","POST"])
def deposit():
    user_id = session["user"]["userid"]

    cur = mysql.connection.cursor()
    cur.execute("SELECT acc_no FROM accounts WHERE user_id=%s",(user_id,))
    accounts = cur.fetchall()
    account=[]
    for acc in accounts:
        account.append(int(acc[0]))

    if request.method == "POST":
        acc_num = request.form["acc_num"]
        amount = request.form["amount"]

        cur = mysql.connection.cursor()

        cur.execute("UPDATE accounts SET balance = balance + %s WHERE acc_no=%s",(amount,acc_num))

        cur.execute("""INSERT INTO transactions (acc_no, amount, type, user_id) VALUES (%s,%s,'Deposit',%s)""",(acc_num,amount,user_id))

        mysql.connection.commit()
        flash("Deposit successfull")
        return redirect(url_for("dashboard"))
    
    return render_template("deposit.html",accounts=account)

@app.route("/withdraw", methods=["GET","POST"])
def withdraw():
    user_id = session["user"]["userid"]

    cur = mysql.connection.cursor()
    cur.execute("SELECT acc_no FROM accounts WHERE user_id=%s",(user_id,))
    accounts = cur.fetchall()
    account=[]
    for acc in accounts:
        account.append(int(acc[0]))

    if request.method == "POST":
        acc_num = request.form["acc_num"]
        amount = request.form["amount"]
        tpin = request.form["tpin"]
        tpin=int(tpin)
        cur = mysql.connection.cursor()
        cur.execute("SELECT t_pin FROM accounts WHERE acc_no=%s",(acc_num,))
        pin = cur.fetchone()
        t_pin=int(pin[0])
        if (tpin!=t_pin) :
            flash("Incorrect Transaction Pin")
            return redirect(url_for("withdraw"))
        
        cur.execute("SELECT balance FROM accounts WHERE acc_no=%s",(acc_num,))
        bal = cur.fetchone()
        balance=int(bal[0])
        amount=int(amount)
        if (balance<amount) :
            flash("Insufficient balance")
            return redirect(url_for("withdraw"))
        
        cur.execute("UPDATE accounts SET balance = balance - %s WHERE acc_no=%s",(amount,acc_num))

        cur.execute("""INSERT INTO transactions (acc_no, amount, type, user_id) VALUES (%s,%s,'Withdraw',%s)""",(acc_num,amount,user_id))

        mysql.connection.commit()
        flash("Withdraw successful")
        return redirect(url_for("dashboard"))

    return render_template("withdraw.html",accounts=account)



@app.route("/create_account", methods=["GET","POST"])
def create_account():
    if request.method == "POST":
        user_id = session["user"]["userid"]
        acc_type = request.form["acc_type"]
        balance = request.form["in_balance"]
        tpin = request.form["tpin"]

        cur = mysql.connection.cursor()
        cur.execute("""SELECT acc_no FROM accounts""")
        accs=cur.fetchall()
        key=True
        while(key):
            acc_no=random.randint(100000000000, 999999999999)
            key=False
            for i in accs:
                acc_t_no=int(i[0])
                if acc_t_no==acc_no:
                    key=True

        cur.execute("""INSERT INTO accounts (acc_no,user_id, type, balance, t_pin) VALUES (%s,%s,%s,%s,%s)""",(acc_no,user_id,acc_type,balance,tpin))

        mysql.connection.commit()
        flash("Account Successfully Opened")
        return redirect(url_for("dashboard"))

    return render_template("create_account.html")

@app.route("/transactions")
def transactions():
    user_id = session["user"]["userid"]

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM transactions WHERE user_id=%s",(user_id,))

    data = cur.fetchall()
    return render_template("transactions.html", data=data)

@app.route("/export")
def export():
    user_id = session["user"]["userid"]

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM transactions WHERE user_id=%s",(user_id,))
    data = cur.fetchall()

    def generate():
        yield "txn_id,acc_no,amount,type,timestamp\n"
        for row in data:
            yield f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n"

    return Response(generate(), mimetype='text/csv',
        headers={"Content-Disposition": "attachment;filename=transactions.csv"})

if __name__ == "__main__":
    app.run(debug=True)