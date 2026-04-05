# result.py — All functions related to student results

from database import get_connection
from utils import calculate_grade, print_header, print_line

def add_result():
    # Add subject wise marks for a student
    print_header("ADD RESULT")
    
    roll_no = input("Student Roll Number: ")
    
    # Find student first
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
    
    semester      = int(input("Semester: "))
    subject       = input("Subject Name: ")
    total_marks   = float(input("Total Marks: "))
    marks_obtained = float(input("Marks Obtained: "))
    exam_date     = input("Exam Date (DD-MM-YYYY): ")
    
    # Auto calculate grade using our utils function
    grade = calculate_grade((marks_obtained / total_marks) * 100)
    
    # INSERT result into database
    cursor.execute("""
        INSERT INTO results (student_id, semester, subject, marks_obtained, total_marks, grade, exam_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (student_id, semester, subject, marks_obtained, total_marks, grade, exam_date))
    
    connection.commit()
    connection.close()
    print(f"✅ Result added. Grade: {grade}")

def view_results():
    # View full result card for a student
    print_header("VIEW RESULTS")
    roll_no  = input("Enter Roll Number: ")
    semester = int(input("Enter Semester: "))
    
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
    print(f"\nResult Card: {student[1]} | Semester {semester}")
    print_line()
    
    # Get all subjects for this semester
    cursor.execute("""
        SELECT subject, marks_obtained, total_marks, grade, exam_date 
        FROM results 
        WHERE student_id = ? AND semester = ?
    """, (student_id, semester))
    
    records = cursor.fetchall()
    connection.close()
    
    if not records:
        print("No results found for this semester.")
        return
    
    total_obtained = 0
    total_possible = 0
    
    for r in records:
        print(f"Subject : {r[0]}")
        print(f"Marks   : {r[1]} / {r[2]}")
        print(f"Grade   : {r[3]}")
        print(f"Date    : {r[4]}")
        print_line()
        total_obtained += r[1]
        total_possible += r[2]
    
    # Calculate overall percentage
    percentage = (total_obtained / total_possible) * 100
    overall_grade = calculate_grade(percentage)
    
    print(f"Overall : {total_obtained} / {total_possible}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Overall Grade : {overall_grade}") 