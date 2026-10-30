# Write a Python script to insert multiple user records into the MySQL database using executemany() method.
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor()

sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
users_data = [
    ("Aarav", "aarav@example.com"),
    ("Priya", "priya@example.com"),
    ("Rahul", "rahul@example.com")
]

cursor.executemany(sql, users_data)
conn.commit()

print(f"{cursor.rowcount} records inserted successfully using executemany().")
cursor.close()
conn.close()