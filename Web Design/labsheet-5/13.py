# Write a Python script to log database error messages and access timestamps into a dedicated server log file.
import datetime

def log_error(error_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {error_message}\n"
    with open("db_error.log", "a") as log_file:
        log_file.write(log_entry)

# Example usage
log_error("Sample database connection failure simulation.")
print("Error logged successfully into db_error.log")