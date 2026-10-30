# Implement a Python script to update user profile information in MySQL based on a given user ID.
import mysql.connector

conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
cursor = conn.cursor()

user_id = 1
new_email = "updated_aarav@example.com"

sql = "UPDATE users SET email = %s WHERE id = %s"
cursor.execute(sql, (new_email, user_id))
conn.commit()

print(f"User ID {user_id} updated successfully!")
cursor.close()
conn.close()