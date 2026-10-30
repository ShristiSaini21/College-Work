# Write a Python script to connect to a MySQL database server and execute a query returning the database server version.
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='college_db',
        user='root',
        password=''
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print(f"Connected to MySQL Server version: {db_Info}")
except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")