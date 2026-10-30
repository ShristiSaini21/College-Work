# Create a Python script that connects to MySQL and creates a database named `python_web_db` with a table `users`.
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='')
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS python_web_db")
cursor.execute("USE python_web_db")

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
""")
print("Database 'python_web_db' and 'users' table created successfully!")
cursor.close()
conn.close()