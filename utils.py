# utils.py — Helper functions used across the whole system

def calculate_grade(marks):
    # This function takes marks as input and returns the correct grade
    # Think of it like a college grading chart
    
    if marks >= 90:
        return "A+"   # Excellent
    elif marks >= 80:
        return "A"    # Very Good
    elif marks >= 70:
        return "B+"   # Good
    elif marks >= 60:
        return "B"    # Above Average
    elif marks >= 50:
        return "C"    # Average
    elif marks >= 40:
        return "D"    # Below Average
    else:
        return "F"    # Fail

def print_line():
    # Prints a divider line — used to make terminal output look clean
    print("-" * 50)

def print_header(title):
    # Prints a formatted header for each section
    print_line()
    print(f"   {title}")
    print_line()