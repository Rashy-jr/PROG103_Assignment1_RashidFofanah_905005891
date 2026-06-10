# Student Record Management System

students = []

# Function to add student
def add_student():
    name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")
    marks = float(input("Enter Marks: "))

    student = {
        "name": name,
        "id": student_id,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")

# Function to view students
def view_students():
    if len(students) == 0:
        print("No student records available.")
    else:
        print("\n----- Student Records -----")

        for student in students:
            print("Name:", student["name"])
            print("ID:", student["id"])
            print("Marks:", student["marks"])
            print("--------------------------")

# Function to search student
def search_student():
    search_id = input("Enter Student ID to search: ")

    found = False

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            found = True

    if not found:
        print("Student not found.")

# Function to calculate average marks
def average_marks():
    if len(students) == 0:
        print("No student records available.")
    else:
        total = 0

        for student in students:
            total += student["marks"]

        average = total / len(students)

        print("Average Marks:", average)

# Main Program
while True:

    print("\n================================")
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        average_marks()

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice.")