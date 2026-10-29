#1. create and write text into a file
'''with open("sample.txt", "w") as f:
   f.write("Hello Python File Handling\nThis is a sample text file.")
print("File created and text written successfully.")'''

#2. read the entire content of a text file
'''with open("sample.txt", "r") as f:
   content = f.read()
print("File Content:\n", content)'''

#3. read a file line by line
'''with open("sample.txt", "r") as f:
   for line in f:
       print(line.strip())'''

#4. count the number of words in a text file
'''with open("sample.txt", "r") as f:
   text = f.read()
   words = text.split()
print("Total word count:", len(words))'''

#5. count the number of lines and characters in a file
'''with open("sample.txt", "r") as f:
   lines = f.readlines()
   num_lines = len(lines)
   num_chars = sum(len(line) for line in lines)
print(f"Lines: {num_lines}, Characters: {num_chars}")'''

#6. display only even-numbered lines from a file
'''with open("sample.txt", "r") as f:
   for index, line in enumerate(f, start=1):
       if index % 2 == 0:
           print(f"Line {index}: {line.strip()}")'''

#7. write multiple lines of input from the user into a file
'''lines = ["First line\n", "Second line\n", "Third line\n"]
with open("user_input.txt", "w") as f:
f.writelines(lines)
print("Multiple lines written to file.")'''

#8. append new content to an existing file
'''with open("sample.txt", "a") as f:
f.write("\nAppended new content to file.")
print("Content appended successfully.")'''

#9. copy the contents of one file into another
'''with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
dest.write(src.read())
print("File copied successfully.")'''

#10. read a file and convert its content to uppercase
'''with open("sample.txt", "r") as f:
upper_content = f.read().upper()
print("Uppercase Content:\n", upper_content)'''

#11. search for a particular word in a file
'''word = "Python"
with open("sample.txt", "r") as f:
text = f.read()
if word in text:
print(f"'{word}' found in the file.")
else:
print(f"'{word}' not found in the file.")'''

#12. count the occurrence of a specific word in a file
'''target_word = "Python"
with open("sample.txt", "r") as f:
words = f.read().split()
count = words.count(target_word)
print(f"The word '{target_word}' appears {count} times.")'''

#13. read numbers from a file and display their sum and average
'''with open("numbers.txt", "r") as f:
nums = [float(line.strip()) for line in f if line.strip()]
total = sum(nums)
avg = total / len(nums) if nums else 0
print(f"Sum: {total}, Average: {avg}")'''

#14. display the longest line in a file
'''with open("sample.txt", "r") as f:
lines = [line.strip() for line in f]
longest = max(lines, key=len) if lines else ""
print("Longest line:", longest)'''

#15. replace a word in a file with another word
'''with open("sample.txt", "r") as f:
content = f.read()
new_content = content.replace("sample", "example")
with open("sample.txt", "w") as f:
f.write(new_content)
print("Word replaced successfully.")'''

#16. display the first and last lines of a file
'''with open("sample.txt", "r") as f:
lines = [line.strip() for line in f]
if lines:
print("First line:", lines[0])
print("Last line:", lines[-1])'''

#17. remove blank lines from a file
'''with open("sample.txt", "r") as f:
lines = f.readlines()
non_empty_lines = [line for line in lines if line.strip()]
with open("cleaned.txt", "w") as f:
f.writelines(non_empty_lines)
print("Blank lines removed.")'''

#18. read a file and store only unique words into another file
'''with open("sample.txt", "r") as f:
words = f.read().split()
unique_words = sorted(set(words))
with open("unique_words.txt", "w") as f:
f.write("\n".join(unique_words))
print("Unique words saved.")'''

#19. sort all words in a file alphabetically and save to a new file
'''with open("sample.txt", "r") as f:
words = f.read().split()
sorted_words = sorted(words)
with open("sorted_words.txt", "w") as f:
f.write("\n".join(sorted_words))
print("Sorted words saved.")'''

#20. merge two text files into a third file
'''with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", 
"w") as f3:
f3.write(f1.read() + "\n" + f2.read())
print("Files merged successfully.")'''

#21. create and write data into a CSV file
'''import csv
data = [["Name", "Marks"], ["Rahul", 85], ["Priya", 92], ["Amit", 78]]
with open("students.csv", "w", newline="") as f:
writer = csv.writer(f)
writer.writerows(data)
print("CSV file created.")'''

#22. read data from a CSV file and display it
'''import csv
with open("students.csv", "r") as f:
reader = csv.reader(f)
for row in reader:
print(row)'''

#23. read a CSV file and calculate the average of numeric columns
'''import csv
with open("students.csv", "r") as f:
reader = csv.reader(f)
next(reader) # skip header
marks = [float(row[1]) for row in reader if row]
avg_marks = sum(marks) / len(marks) if marks else 0
print("Average Marks:", avg_marks)'''

#24. count the number of rows and columns in a CSV file
'''import csv
with open("students.csv", "r") as f:
rows = list(csv.reader(f))
num_rows = len(rows)
num_cols = len(rows[0]) if rows else 0
print(f"Rows: {num_rows}, Columns: {num_cols}")'''

#25. append a new record to an existing CSV file
'''import csv
new_record = ["Suman", 88]
with open("students.csv", "a", newline="") as f:
   writer = csv.writer(f)
   writer.writerow(new_record)
print("Record appended to CSV.")'''

#26. copy data from one CSV file to another
'''import csv
with open("students.csv", "r") as src, open("students_copy.csv", "w", newline="") as des
t:
   reader = csv.reader(src)
   writer = csv.writer(dest)
   for row in reader:
       writer.writerow(row)
print("CSV copied successfully.")'''

#27. display specific columns (like Name and Marks) from a CSV file
'''import csv
with open("students.csv", "r") as f:
   reader = csv.DictReader(f)
   for row in reader:
       print(f"Name: {row['Name']}, Marks: {row['Marks']}")'''

#28. find and display the highest marks from a CSV file
'''import csv
with open("students.csv", "r") as f:
   reader = csv.DictReader(f)
   top_student = max(reader, key=lambda x: float(x['Marks']))
print(f"Highest Marks: {top_student['Name']} with {top_student['Marks']}")'''

#29. search a record in a CSV file based on student name
'''import csv
search_name = "Priya"
with open("students.csv", "r") as f:
   reader = csv.DictReader(f)
   for row in reader:
       if row['Name'].lower() == search_name.lower():
           print("Record Found:", row)
           break'''

#30. combine multiple CSV files into one single file
'''import csv
files = ["students.csv", "students_copy.csv"]
with open("combined.csv", "w", newline="") as outfile:
   writer = csv.writer(outfile)
   for idx, fname in enumerate(files):
       with open(fname, "r") as infile:
           reader = csv.reader(infile)
           header = next(reader)
           if idx == 0:
               writer.writerow(header)
           for row in reader:
               writer.writerow(row)
it("CSVfil bi d fll ")'''
