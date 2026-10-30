# Test Apache and Python integration by creating a dynamic web endpoint that generates JSON responses from MySQL queries.
import json
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Content-Type: application/json\n")
print(json.dumps(rows))

cursor.close()
conn.close()