# Write a Python CGI script that reads form input data via `cgi` module and inserts the submitted data into MySQL.
import cgi
import mysql.connector

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
username = form.getvalue("username")
email = form.getvalue("email")

if username and email:
    try:
        conn = mysql.connector.connect(host='localhost', database='python_web_db', user='root', password='')
        cursor = conn.cursor()
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(sql, (username, email))
        conn.commit()
        print(f"<p>User {username} inserted successfully via CGI!</p>")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"<p>Error: {e}</p>")
else:
    print("""
        <form method='POST'>
            Username: <input type='text' name='username'><br>
            Email: <input type='text' name='email'><br>
            <button type='submit'>Submit</button>
        </form>
    """)