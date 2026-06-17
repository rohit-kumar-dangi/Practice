# Write a program to perform INSERT, UPDATE, DELETE, and SELECT operations on a database.

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
conn = mysql.connector.connect(
    host= os.getenv('DB_HOST'),
    user= os.getenv('DB_USER'),
    password= os.getenv('DB_PASSWORD'),
    database= os.getenv('DB_NAME')
)

cursor = conn.cursor()

# INSERT
cursor.execute("INSERT INTO student VALUES (1, 'Rohit', 80)")

# UPDATE
cursor.execute("UPDATE student SET marks = 90 WHERE id = 1")

# SELECT
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

# DELETE
cursor.execute("DELETE FROM student WHERE id = 1")

conn.commit()
conn.close()