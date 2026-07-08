from database import insert_student, view_students, search_student, update_student, delete_student


def add_student():
    name = input("Enter your name: ")
    if name.strip() == "":
     print("Name cannot be empty.")
     return
    try:    
     age = int(input("Enter your age: "))
    except ValueError:
      print("Invalid age! Please enter a number.")
      return   
    course = input("Enter your course: ")
    if course.strip() == "":
     print("Course cannot be empty.")
     return
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
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

while True:
    menu()
    try:    
     choice = int(input("Enter your choice: "))
    except ValueError:
      print("Invalid choice! Please enter a number.")
      continue
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3 :
        name = input("Enter student name: ")
        search_student(name) 
    elif choice == 4:
        try:
         student_id = int(input("Enter Student ID: "))
         age = int(input("Enter New Age: "))
        except ValueError:
         print("Student ID and Age must be numbers.")
         continue
        course = input("Enter New Course: ")  
        update_student(student_id, age, course)
        print("Student updated successfully!") 
    elif choice == 5:
        try:
         student_id = int(input("Enter Student ID to delete: "))
        except ValueError:
         print("Student ID must be a number.")
         continue

        delete_student(student_id)

        print("Student deleted successfully!")
    elif choice == 6:
     print("Thank you for using Student Management System.")
     break
    else :
      print("Invalid choice. Please try again.")