# fees.py — All functions related to fee management

from database import get_connection
from utils import print_header, print_line

def add_fee_record():
    # Add a fee record for a student for a specific semester
    print_header("ADD FEE RECORD")
    
    roll_no    = input("Student Roll Number: ")
    
    # First find the student ID from roll number
    connection = get_connection()
    cursor     = connection.cursor()
    cursor.execute("SELECT id, name FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()
    
    if not student:
        print("❌ Student not found.")
        connection.close()
        return
    
    student_id   = student[0]  # get the ID
    student_name = student[1]  # get the name
    print(f"Student Found: {student_name}")
    
    semester     = int(input("Semester: "))
    amount_due   = float(input("Total Fee Amount Due (₹): "))
    amount_paid  = float(input("Amount Paid (₹): "))
    payment_date = input("Payment Date (DD-MM-YYYY): ")
    
    # Automatically determine status based on amounts
    if amount_paid >= amount_due:
        status = "Paid"
    elif amount_paid > 0:
        status = "Partial"
    else:
        status = "Pending"
    
    # INSERT the fee record
    cursor.execute("""
        INSERT INTO fees (student_id, semester, amount_due, amount_paid, payment_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (student_id, semester, amount_due, amount_paid, payment_date, status))
    
    connection.commit()
    connection.close()
    print(f"✅ Fee record added. Status: {status}")

def view_fee_status():
    # View fee status for a specific student
    print_header("FEE STATUS")
    roll_no = input("Enter Roll Number: ")
    
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
    print(f"\nFee Records for: {student[1]}")
    print_line()
    
    # Get all fee records for this student
    # JOIN would be better here but we'll keep it simple
    cursor.execute("SELECT semester, amount_due, amount_paid, payment_date, status FROM fees WHERE student_id = ?", (student_id,))
    records = cursor.fetchall()
    connection.close()
    
    if not records:
        print("No fee records found.")
        return
    
    total_due  = 0
    total_paid = 0
    
    for r in records:
        print(f"Semester {r[0]} | Due: ₹{r[1]} | Paid: ₹{r[2]} | Date: {r[3]} | Status: {r[4]}")
        total_due  += r[1]
        total_paid += r[2]
    
    print_line()
    print(f"Total Due : ₹{total_due}")
    print(f"Total Paid: ₹{total_paid}")
    print(f"Balance   : ₹{total_due - total_paid}")

def view_pending_fees():
    # Show all students with pending or partial fees
    print_header("PENDING FEES")
    
    connection = get_connection()
    cursor     = connection.cursor()
    
    # This query joins students and fees tables to get names with pending fees
    cursor.execute("""
        SELECT students.name, students.roll_no, fees.semester, fees.amount_due, fees.amount_paid, fees.status
        FROM fees
        JOIN students ON fees.student_id = students.id
        WHERE fees.status != 'Paid'
    """)
    
    records = cursor.fetchall()
    connection.close()
    
    if not records:
        print("✅ No pending fees.")
        return
    
    for r in records:
        print(f"{r[0]} | Roll: {r[1]} | Sem {r[2]} | Due: ₹{r[3]} | Paid: ₹{r[4]} | {r[5]}")
        print_line()