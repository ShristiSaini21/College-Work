# Write a Python script to delete a record from the MySQL database and handle database exceptions using `try-except` blocks.
import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
    cursor = conn.cursor()
    
    user_id = 2
    sql = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql, (user_id,))
    conn.commit()
    print(f"Record with ID {user_id} deleted successfully.")

except mysql.connector.Error as err:
    print(f"Database error occurred: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()