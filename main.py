# main.py — The main menu that connects all modules together

import os  # to create the data folder if it doesn't exist

# Import the database setup function
from database import create_tables

# Import all student functions
from student import add_student, view_all_students, search_student, update_student, delete_student

# Import all fee functions
from fees import add_fee_record, view_fee_status, view_pending_fees

# Import all result functions
from result import add_result, view_results

# Import all attendance functions
from attendence import mark_attendance, view_attendance

# Import helpers
from utils import print_header, print_line

def main_menu():
    # The main menu — keeps running until user exits
    while True:
        print("\n")
        print_line()
        print("   🎓 COLLEGE MANAGEMENT SYSTEM")
        print_line()
        print("  1. Student Management")
        print("  2. Fee Management")
        print("  3. Results Management")
        print("  4. Attendance Management")
        print("  5. Exit")
        print_line()
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            student_menu()
        elif choice == "2":
            fee_menu()
        elif choice == "3":
            result_menu()
        elif choice == "4":
            attendance_menu()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice.")

def student_menu():
    # Sub menu for student management
    while True:
        print_header("STUDENT MANAGEMENT")
        print("  1. Add New Student")
        print("  2. View All Students")
        print("  3. Search Student")
        print("  4. Update Student")
        print("  5. Delete Student")
        print("  6. Back to Main Menu")
        print_line()
        
        choice = input("Choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice.")

def fee_menu():
    # Sub menu for fee management
    while True:
        print_header("FEE MANAGEMENT")
        print("  1. Add Fee Record")
        print("  2. View Student Fee Status")
        print("  3. View All Pending Fees")
        print("  4. Back to Main Menu")
        print_line()
        
        choice = input("Choice: ")
        
        if choice == "1":
            add_fee_record()
        elif choice == "2":
            view_fee_status()
        elif choice == "3":
            view_pending_fees()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice.")

def result_menu():
    # Sub menu for results management
    while True:
        print_header("RESULTS MANAGEMENT")
        print("  1. Add Result")
        print("  2. View Result Card")
        print("  3. Back to Main Menu")
        print_line()
        
        choice = input("Choice: ")
        
        if choice == "1":
            add_result()
        elif choice == "2":
            view_results()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice.")

def attendance_menu():
    # Sub menu for attendance management
    while True:
        print_header("ATTENDANCE MANAGEMENT")
        print("  1. Mark Attendance")
        print("  2. View Attendance")
        print("  3. Back to Main Menu")
        print_line()
        
        choice = input("Choice: ")
        
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice.")

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create all database tables when app starts
create_tables()

# Launch the main menu
main_menu()