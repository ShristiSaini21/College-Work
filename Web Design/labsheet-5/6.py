# Develop a Python script that retrieves all records from the `users` table and formats them into an HTML response string.
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

html_output = "<h2>User Records</h2><table border='1'><tr><th>ID</th><th>Username</th><th>Email</th></tr>"
for row in results:
    html_output += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
html_output += "</table>"

print("Content-Type: text/html\n")
print(html_output)

cursor.close()
conn.close()