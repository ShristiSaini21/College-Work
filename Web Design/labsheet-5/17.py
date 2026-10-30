# Write a Python script to backup a MySQL database schema and data into a `.sql` file programmatically.
import os

db_user = "root"
db_name = "python_web_db"
backup_file = "backup.sql"

# Using mysqldump utility programmatically
cmd = f"mysqldump -u {db_user} {db_name} > {backup_file}"
os.system(cmd)

print(f"Database backup completed to {backup_file}")