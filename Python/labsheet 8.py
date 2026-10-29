#1. connect to a database and display success message
'''import sqlite3
try:
   conn = sqlite3.connect("student_db.db")
   print("Successfully connected to database.")
   conn.close()
except Exception as e:
   print("Database error:", e)'''

#2. create a new database
'''import sqlite3
conn = sqlite3.connect("college_db.db")
print("New database 'college_db' created successfully.")
conn.close()'''

#3. create a new table named students
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("""
   CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY,
       name TEXT,
       age INTEGER,
       marks REAL
   )
""")
conn.commit()
print("Table 'students' created successfully.")
conn.close()'''

#4. describe the structure of the students table
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(students)")
columns = cursor.fetchall()
for col in columns:
   print(f"Col: {col[1]}, Type: {col[2]}")
conn.close()'''

#5. list all tables available in the connected database
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)
conn.close()'''

#6. drop (delete) a table from the database
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS temp_table")
it()'''

#7. check if a specific table exists in the database
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
exists = cursor.fetchone() is not None
print("Students table exists:", exists)
conn.close()'''

#8. insert a single record into the students table
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO students VALUES (1, 'Rahul', 21, 85.5)")
conn.commit()
print("Record inserted successfully.")
conn.close()'''

#9. insert multiple records into the students table
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
records = [
(2, 'Priya', 20, 92.0),
(3, 'Amit', 22, 78.0),
(4, 'Suman', 21, 88.5),
(5, 'Rohan', 19, 35.0)
]
cursor.executemany("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)", records)
conn.commit()
print("Multiple records inserted.")
conn.close()'''

#10. read and display all records from the table
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
print(row)
conn.close()'''

#11. display only specific columns (like name and marks)
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT name, marks FROM students")
for name, marks in cursor.fetchall():
print(f"Name: {name}, Marks: {marks}")
conn.close()'''

#12. retrieve records where marks are greater than 80
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students WHERE marks > 80")
for row in cursor.fetchall():
    print(row)
conn.close()'''

#13. retrieve data sorted by marks in descending order
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students ORDER BY marks DESC")
for row in cursor.fetchall():
print(row)
conn.close()'''

#14. count the total number of records in the table
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM students")
total = cursor.fetchone()[0]
print("Total records:", total)
conn.close()'''

#15. display the top 3 highest scoring students
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
for row in cursor.fetchall():
print(row)
conn.close()'''

#16. update the marks of a student using their ID
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("UPDATE students SET marks = 89.0 WHERE id = 1")
conn.commit()
print("Marks updated successfully.")
conn.close()'''

#17. update the name of a student
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("UPDATE students SET name = 'Rahul Sharma' WHERE id = 1")
conn.commit()
print("Name updated successfully.")
conn.close()'''

#18. delete a student record using ID
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM students WHERE id = 5")
conn.commit()
print("Record deleted successfully.")
conn.close()'''

#19. delete all students with marks below 40
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM students WHERE marks < 40")
conn.commit()
print("Students with marks < 40 deleted.")
conn.close()'''

#20. truncate (empty) a table while keeping structure
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM students")
conn.commit()
print("Table truncated (cleared).")
conn.close()'''

#21. create a table for courses and insert data
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS courses (course_id INT, student_id INT, course
_name TEXT)")
cursor.execute("INSERT INTO courses VALUES (101, 1, 'Python'), (102, 2, 'DBMS')")
conn.commit()
print("Courses table created and populated.")
conn.close()'''

#22. perform an INNER JOIN between students and courses
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
query = "SELECT s.name, c.course_name FROM students s INNER JOIN courses c ON s.id = c.st
udent_id"
cursor.execute(query)
for row in cursor.fetchall():
print(row)
conn.close()'''

#23. perform a LEFT JOIN between students and courses
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
query = "SELECT s.name, c.course_name FROM students s LEFT JOIN courses c ON s.id = c.stu
dent_id"
cursor.execute(query)
for row in cursor.fetchall():
print(row)
conn.close()'''

#24. find the average marks of all students
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT AVG(marks) FROM students")
avg_marks = cursor.fetchone()[0]
print("Average marks of all students:", avg_marks)
conn.close()'''

#25. display students grouped by age and count
'''import sqlite3
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT age, COUNT(*) FROM students GROUP BY age")
for age, count in cursor.fetchall():
   print(f"Age {age}: {count} student(s)")
conn.close()'''

#26. export table data from database into a CSV file
'''import sqlite3, csv
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
with open("exported_students.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerow(["ID", "Name", "Age", "Marks"])
   writer.writerows(rows)
print("Data exported to CSV.")
conn.close()'''

#27. import data from a CSV file into database table
'''import sqlite3, csv
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
with open("exported_students.csv", "r") as f:
   reader = csv.reader(f)
   next(reader)
   for row in reader:
       cursor.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)", row)
conn.commit()
print("Data imported from CSV.")
conn.close()'''

#28. display all database errors using exception handling
'''import sqlite3
try:
   conn = sqlite3.connect("student_db.db")
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.Error as e:
   print("Database Exception Caught:", e)
finally:
   conn.close()'''

#29. use a function to insert and fetch data (modular approach)
'''import sqlite3

def add_student(sid, name, age, marks):
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)", (sid, name, age, marks))
    conn.commit()
    conn.close()

def fetch_students():
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    conn.close()

add_student(1, "Rahul", 20, 85)
fetch_students()'''

#30. create a simple menu-driven application for student management (Add, View, Update, Delete)
'''import sqlite3

def create_table():
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT, name TEXT, age INT, marks REAL)")
    conn.commit()
    conn.close()

create_table()

while True:
    print("\\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
        conn = sqlite3.connect("student_db.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (sid, name, age, marks))
        conn.commit()
        conn.close()
        print("Student added successfully!")
        
    elif choice == '2':
        conn = sqlite3.connect("student_db.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)
        conn.close()
        
    elif choice == '3':
        sid = int(input("Enter ID to update: "))
        new_marks = float(input("Enter new marks: "))
        conn = sqlite3.connect("student_db.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, sid))
        conn.commit()
        conn.close()
        print("Marks updated successfully!")
        
    elif choice == '4':
        sid = int(input("Enter ID to delete: "))
        conn = sqlite3.connect("student_db.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
        conn.commit()
        conn.close()
        print("Student deleted successfully!")
        
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")'''
   
