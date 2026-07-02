from database import insert_student
def add_student():
    name = input("Enter your name :")
    age = int(input("Enter your age :"))
    course = input("Enter your course :")
    
    insert_student(name, age, course)

    print("\nStudent Details")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
add_student()

