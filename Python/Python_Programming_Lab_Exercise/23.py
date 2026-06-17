# Demonstrate transaction control (commit and rollback) in database operations.

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

try:
    cursor.execute("INSERT INTO student VALUES (2, 'Amit', 85)")
    conn.commit()
    print("Transaction committed")

except:
    conn.rollback()
    print("Transaction rolled back")

conn.close()