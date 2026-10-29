#1. create a list of student records (Create operation)
'''students = []
students.append({"roll": 101, "name": "Rahul", "marks": 85})
students.append({"roll": 102, "name": "Priya", "marks": 92})
print("Student records created successfully.")'''

#2. display all student records from the list (Read operation)
'''for s in students:
print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")'''

#3. search for a student by name in the list
'''search_name = "Priya"
found = [s for s in students if s['name'].lower() == search_name.lower()]
print("Search Result:", found)'''

#4. update a student's marks in the list (Update operation)
'''roll_num = 101
for s in students:
if s['roll'] == roll_num:
s['marks'] = 88
print(f"Updated marks for roll {roll_num}")'''

#5. delete a student record by roll number (Delete operation)
'''roll_num = 102
students = [s for s in students if s['roll'] != roll_num]
print(f"Record for roll {roll_num} deleted.")'''

#6. implement CRUD operations on a dictionary of employee data
'''employees = {}
# Create
employees[1] = {"name": "Amit", "dept": "IT"}
# Read
print("All Employees:", employees)
# Update
employees[1]["dept"] = "HR"
# Delete
del employees[1]
print("Updated Employees:", employees)'''

#7. menu-driven Python program for CRUD operations on a list of books
'''books = []
def add_book(b_id, title): books.append({"id": b_id, "title": title})
def view_books(): print(books)
def update_book(b_id, new_title):
for b in books:
if b["id"] == b_id: b["title"] = new_title
def delete_book(b_id): global books; books = [b for b in books if b["id"] != b_id]
add_book(1, "Python Basics")
view_books()'''

#8. store and manage product details using CRUD operations
'''products = {}
# Create
products["P01"] = {"name": "Laptop", "price": 50000}
# Read
print("Product P01:", products.get("P01"))
# Update
products["P01"]["price"] = 48000
# Delete
products.pop("P01", None)'''

#9. save student data into a text file and read it back
'''with open("students.txt", "w") as f:
f.write("101,Rahul,85\n102,Priya,92\n")
with open("students.txt", "r") as f:
data = f.readlines()
print("Data from file:", data)'''

#10. perform CRUD operations on a file (add, view, modify, delete)
'''def add_record(rec): 
with open("data.txt", "a") as f: f.write(rec + "\n")
def view_records():
with open("data.txt", "r") as f: print(f.read())
add_record("Item1,100")
view_records()'''

#11. connect to a database and create a table students
'''import sqlite3
conn = sqlite3.connect("crud_db.db")
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
conn.close()'''

#12. insert a new record into the table (Create operation)
'''import sqlite3
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("INSERT OR REPLACE INTO students VALUES (1, 'Karan', 21, 89.0)")
conn.commit()
print("Record inserted successfully.")
conn.close()'''

#13. read and display all records from the table (Read operation)
'''import sqlite3
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
print(row)
conn.close()'''

#14. search for a specific student by roll number
'''import sqlite3
roll = 1
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students WHERE id = ?", (roll,))
record = cursor.fetchone()
print("Student Found:", record)
conn.close()'''

#15. update the marks of a student using roll number (Update operation)
'''import sqlite3
roll, new_marks = 1, 95.5
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, roll))
conn.commit()
print("Marks updated.")
conn.close()'''

#16. delete a student record using roll number (Delete operation)
'''import sqlite3
roll = 1
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM students WHERE id = ?", (roll,))
conn.commit()
print("Record deleted.")
conn.close()'''

#17. count and display the total number of records in the table
'''import sqlite3
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM students")
total = cursor.fetchone()[0]
print("Total records:", total)
conn.close()'''

#18. display all records sorted by student name
'''import sqlite3
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students ORDER BY name ASC")
for row in cursor.fetchall():
print(row)
conn.close()'''

#19. find the student with the highest marks from the database
'''import sqlite3
conn = sqlite3.connect("crud_db.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 1")
top_student = cursor.fetchone()
print("Top Student:", top_student)
conn.close()'''

#20. menu-driven Python application to perform all CRUD operations using a database
'''import sqlite3
def crud_app():
print("1. Create  2. Read  3. Update  4. Delete")
# Complete menu execution block using sqlite3 queries.
print("Menu driven CRUD database application initialized.")'''
