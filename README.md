# College Management System

A modular CLI-based College Management System built with Python and SQLite.  
It manages student records, attendance, fees, and results with automated grading and performance tracking.

## Features

### Student Management
- Add new students with full details (name, roll number, DOB, Aadhar, phone, email, address, department, semester)
- View all enrolled students
- Search student by roll number
- Update student information
- Delete student records

### Fee Management
- Record semester-wise fee payments
- Auto-detect payment status (Paid / Partial / Pending)
- View complete fee history for any student
- View all students with pending fees

### Results Management
- Add subject-wise marks per semester
- Auto-calculate grade based on marks
- View complete semester result card with percentage and overall grade

### Attendance Management
- Mark daily attendance per subject
- View attendance percentage for any student
- Automatic warning if attendance falls below 75%

## Tech Stack
- Python 3
- SQLite3 (built-in database)
- Modular architecture across 7 files

## Project Structure



## 🚀 How to Run

```bash
git clone https://github.com/biswarup-saha661/college-management-system.git
cd college-management-system
python main.py
## 🖥️ Sample Output
✅ Database and tables ready.


--------------------------------------------------
   🎓 COLLEGE MANAGEMENT SYSTEM
--------------------------------------------------
  1. Student Management
  2. Fee Management
  3. Results Management
  4. Attendance Management
  5. Exit
--------------------------------------------------
Enter your choice (1-5):