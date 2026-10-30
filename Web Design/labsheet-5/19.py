# Write a Python script that verifies and sanitizes incoming web form inputs before executing SQL write operations.
import html
import mysql.connector

def sanitize_input(data):
    return html.escape(data.strip())

raw_username = "   <b>Aarav</b>   "
clean_username = sanitize_input(raw_username)

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor()
cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (clean_username, "sanitized@example.com"))
conn.commit()

print("Sanitized input inserted successfully!")
cursor.close()
conn.close()