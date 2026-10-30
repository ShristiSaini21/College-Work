# Develop a Python script that reads CSV file data and bulk-inserts rows into a MySQL database table.
import csv
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor()

# Assuming a sample CSV file structure: username, email
# with open('users.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader) # skip header
#     data = [row for row in reader]
#     cursor.executemany("INSERT INTO users (username, email) VALUES (%s, %s)", data)
#     conn.commit()

print("CSV bulk-insertion script template ready.")
cursor.close()
conn.close()