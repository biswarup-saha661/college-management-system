# attendence.py — All functions related to attendance

from database import get_connection
from utils import print_header, print_line

def mark_attendance():
    # Mark attendance for a student for a subject on a specific date
    print_header("MARK ATTENDANCE")
    
    roll_no = input("Student Roll Number: ")
    
    # Find student
    connection = get_connection()
    cursor     = connection.cursor()
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()
    
    if not student:
        print("❌ Student not found.")
        connection.close()
        return
    
    student_id   = student[0]
    student_name = student[1]
    print(f"Student Found: {student_name}")
    
    subject = input("Subject: ")
    date    = input("Date (DD-MM-YYYY): ")
    status  = input("Status (Present/Absent): ").capitalize()
    
    # INSERT attendance record
    cursor.execute("""
        INSERT INTO attendance (student_id, subject, date, status)
        VALUES (?, ?, ?, ?)
    """, (student_id, subject, date, status))
    
    connection.commit()
    connection.close()
    print(f"✅ Attendance marked: {status}")

def view_attendance():
    # View attendance percentage for a student in a subject
    print_header("VIEW ATTENDANCE")
    
    roll_no = input("Enter Roll Number: ")
    subject = input("Enter Subject: ")
    
    connection = get_connection()
    cursor     = connection.cursor()
    
    # Find student
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()
    
    if not student:
        print("❌ Student not found.")
        connection.close()
        return
    
    student_id = student[0]
    
    # Count total classes
    cursor.execute("""
        SELECT COUNT(*) FROM attendance 
        WHERE student_id = ? AND subject = ?
    """, (student_id, subject))
    total = cursor.fetchone()[0]
    
    # Count present classes
    cursor.execute("""
        SELECT COUNT(*) FROM attendance 
        WHERE student_id = ? AND subject = ? AND status = 'Present'
    """, (student_id, subject))
    present = cursor.fetchone()[0]
    connection.close()
    
    if total == 0:
        print("No attendance records found.")
        return
    
    # Calculate percentage
    percentage = (present / total) * 100
    
    print_line()
    print(f"Student  : {student[1]}")
    print(f"Subject  : {subject}")
    print(f"Present  : {present} / {total}")
    print(f"Percentage: {percentage:.2f}%")
    
    # Warn if below 75%
    if percentage < 75:
        print("⚠️  WARNING: Attendance below 75%!")
    else:
        print("✅ Attendance is satisfactory.")
    print_line()