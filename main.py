from database import *

# Create the table for the first time
create_table()

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Update Student Data")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Student Name: ")
            age = int(input("Age: "))
            add_student(name, age)

        elif choice == '2':
            show_students()

        elif choice == '3':
            student_id = int(input("Student ID: "))
            new_name = input("New Name: ")
            new_age = int(input("New Age: "))
            update_student(student_id, new_name, new_age)

        elif choice == '4':
            student_id = int(input("Student ID to delete: "))
            delete_student(student_id)

        elif choice == '5':
            print("Exited successfully.")
            break

        else:
            print("Invalid choice, please try again!")

menu()
