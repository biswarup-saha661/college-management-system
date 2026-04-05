# student.py — All functions related to student management

from database import get_connection  # import our connection function
from utils import calculate_grade, print_header, print_line  # import helpers

def add_student():
    # This function collects student info and saves it to the database
    print_header("ADD NEW STUDENT")
    
    # Collect all details from user input
    name          = input("Full Name: ")
    roll_no       = input("Roll Number: ")
    dob           = input("Date of Birth (DD-MM-YYYY): ")
    gender        = input("Gender (Male/Female/Other): ")
    phone         = input("Phone Number: ")
    email         = input("Email: ")
    aadhar_no     = input("Aadhar Number: ")
    address       = input("Address: ")
    admission_date = input("Admission Date (DD-MM-YYYY): ")
    department    = input("Department (CSE/ECE/ME/CE): ")
    semester      = int(input("Current Semester (1-8): "))

    # Open database connection
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # INSERT query — adds a new row to the students table
        cursor.execute("""
            INSERT INTO students 
            (name, roll_no, dob, gender, phone, email, aadhar_no, address, admission_date, department, semester)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, roll_no, dob, gender, phone, email, aadhar_no, address, admission_date, department, semester))
        
        connection.commit()  # save the new record
        print(f"\n✅ Student '{name}' added successfully with Roll No: {roll_no}")
    
    except Exception as e:
        # If roll number already exists, this will catch the error
        print(f"\n❌ Error: {e}")
    
    finally:
        connection.close()  # always close the connection

def view_all_students():
    # This function fetches and displays all students
    print_header("ALL STUDENTS")
    
    connection = get_connection()
    cursor = connection.cursor()

    # SELECT * means — give me all columns from students table
    cursor.execute("SELECT id, name, roll_no, department, semester, phone FROM students")
    students = cursor.fetchall()  # fetchall() returns all matching rows as a list
    connection.close()

    if not students:
        print("No students found.")
        return

    # Print each student in a neat format
    for s in students:
        print(f"[{s[0]}] {s[1]} | Roll: {s[2]} | {s[3]} | Sem {s[4]} | Phone: {s[5]}")
        print_line()

def search_student():
    # Search a student by roll number
    print_header("SEARCH STUDENT")
    roll_no = input("Enter Roll Number: ")

    connection = get_connection()
    cursor = connection.cursor()

    # WHERE clause filters — only returns the student with this roll number
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
    s = cursor.fetchone()  # fetchone() returns just one row
    connection.close()

    if not s:
        print("❌ Student not found.")
        return

    # Display full student profile
    print_line()
    print(f"  ID            : {s[0]}")
    print(f"  Name          : {s[1]}")
    print(f"  Roll No       : {s[2]}")
    print(f"  Date of Birth : {s[3]}")
    print(f"  Gender        : {s[4]}")
    print(f"  Phone         : {s[5]}")
    print(f"  Email         : {s[6]}")
    print(f"  Aadhar No     : {s[7]}")
    print(f"  Address       : {s[8]}")
    print(f"  Admission Date: {s[9]}")
    print(f"  Department    : {s[10]}")
    print(f"  Semester      : {s[11]}")
    print_line()

def update_student():
    # Update a student's semester or phone number
    print_header("UPDATE STUDENT")
    roll_no = input("Enter Roll Number to update: ")

    print("What do you want to update?")
    print("1. Phone Number")
    print("2. Semester")
    print("3. Address")
    choice = input("Choice: ")

    connection = get_connection()
    cursor = connection.cursor()

    if choice == "1":
        new_phone = input("New Phone Number: ")
        # UPDATE query — changes only the phone of this specific student
        cursor.execute("UPDATE students SET phone = ? WHERE roll_no = ?", (new_phone, roll_no))
    elif choice == "2":
        new_sem = int(input("New Semester: "))
        cursor.execute("UPDATE students SET semester = ? WHERE roll_no = ?", (new_sem, roll_no))
    elif choice == "3":
        new_address = input("New Address: ")
        cursor.execute("UPDATE students SET address = ? WHERE roll_no = ?", (new_address, roll_no))

    connection.commit()
    connection.close()
    print("✅ Student updated successfully.")

def delete_student():
    # Permanently delete a student record
    print_header("DELETE STUDENT")
    roll_no = input("Enter Roll Number to delete: ")
    confirm = input(f"Are you sure you want to delete {roll_no}? (yes/no): ")

    if confirm.lower() != "yes":
        print("Cancelled.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    # DELETE query — removes this student from the table permanently
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    connection.commit()
    connection.close()
    print("✅ Student deleted successfully.")