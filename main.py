from database import insert_student, view_students,search_student, update_student, delete_student,sort_students,count_students,search_by_age_course,search_by_age_or_course,search_student_partial,average_age, maximum_age,minimum_age,total_age,unique_courses,students_by_course


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
    print("6. Sort Students by Age")
    print("7. Count Students")
    print("8. Search by Age and Course")
    print("9. Search by Age OR Course")
    print("10. Partial Name Search")
    print("11. Average Age")
    print("12. Maximum Age")
    print("13. Minimum Age")
    print("14. Show Available Courses")
    print("15. Students by Course")
    print("16. Exit")

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
        if course.strip() == "":
            print("Course cannot be empty.")
            continue 
        update_student(student_id, age, course)
    elif choice == 5:
        try:
         student_id = int(input("Enter Student ID to delete: "))
        except ValueError:
         print("Student ID must be a number.")
         continue

        delete_student(student_id)
    elif choice == 6:
      sort_students()
    elif choice == 7:
      count_students()

    elif choice == 8:
       try:
        age = int(input("Enter age : "))
       except ValueError: 
        print("Student Age must be a number.")
        continue
       course = input("Enter course : ")
       if course.strip() == "":
        print("Course cannot be empty.")
        continue
       search_by_age_course(age, course)

    elif choice == 9:
        try:
         age = int(input("Enter age : "))
        except ValueError: 
         print("Student Age must be a number.")
         continue
        course = input("Enter course : ")
        if course.strip() == "":
         print("Course cannot be empty.")
         continue
        search_by_age_or_course(age, course)
    elif choice == 10:
      name = input("Enter name : ")
      search_student_partial(name)
    elif choice == 11:
        average_age() 
    elif choice == 12:
       maximum_age()
    elif choice == 13:
        minimum_age()
    elif choice == 14:
       unique_courses()        
    elif choice == 15:
      students_by_course()
    elif choice == 16:
     print("Thank you for using Student Management System.")
     break
    else :
      print("Invalid choice. Please try again.")