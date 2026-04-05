# database.py — Handles all database connection and table creation

import sqlite3  # sqlite3 is built into Python — no installation needed

DATABASE = "data/college.db"  # this is where our database file will be saved

def get_connection():
    # This function opens a connection to the database
    # Think of it like opening an Excel file
    connection = sqlite3.connect(DATABASE)
    return connection

def create_tables():
    # This function creates all our tables if they don't exist yet
    # IF NOT EXISTS means — only create if it's not already there
    # So running this 100 times won't cause any errors
    
    connection = get_connection()  # open the database
    cursor = connection.cursor()   # create a cursor — like a pen to write SQL

    # TABLE 1 — Students (master record of every student)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT UNIQUE NOT NULL,
            dob TEXT,
            gender TEXT,
            phone TEXT,
            email TEXT,
            aadhar_no TEXT,
            address TEXT,
            admission_date TEXT,
            department TEXT,
            semester INTEGER
        )
    """)

    # TABLE 2 — Fees (tracks fee payment per semester)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            semester INTEGER,
            amount_due REAL,
            amount_paid REAL,
            payment_date TEXT,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # TABLE 3 — Results (subject wise marks per semester)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            semester INTEGER,
            subject TEXT,
            marks_obtained REAL,
            total_marks REAL,
            grade TEXT,
            exam_date TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # TABLE 4 — Attendance (daily attendance per subject)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT,
            date TEXT,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    connection.commit()  # save all changes
    connection.close()   # close the database
    print("✅ Database and tables ready.")