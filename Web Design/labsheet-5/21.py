# Write a Python script to generate analytical summary reports (counts, averages) from MySQL data for administrative dashboards.
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) AS total_users FROM users")
result = cursor.fetchone()

print("--- Administrative Dashboard Report ---")
print(f"Total Registered Users: {result[0]}")

cursor.close()
conn.close()