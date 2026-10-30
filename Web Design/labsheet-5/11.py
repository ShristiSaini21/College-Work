# Write a Python script that connects to MySQL, performs a parameterized query to prevent SQL injection, and returns filtered results.
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor()

search_name = "Aarav"
sql = "SELECT * FROM users WHERE username = %s"
cursor.execute(sql, (search_name,))
result = cursor.fetchall()

print("Filtered Query Results:")
for row in result:
    print(row)

cursor.close()
conn.close()