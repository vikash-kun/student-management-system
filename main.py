from database import insert_student, view_students, search_student


def add_student():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    course = input("Enter your course: ")

    insert_student(name, age, course)

    print("\nStudent Details")
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")

def menu():
    print("========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3" :
        name = input("Enter student name: ")
        search_student(name)  
    elif choice == "4":
     print("Thank you for using Student Management System.")
     break
    else :
        print("Invalid choice. Please try again.")