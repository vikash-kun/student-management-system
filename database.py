import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

connection.commit()
connection.close()


def insert_student(name, age, course):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    connection.commit()
    connection.close()

def view_students():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if students:
        for student in students:
            student_id, name, age, course = student

            print(f"ID     : {student_id}")
            print(f"Name   : {name}")
            print(f"Age    : {age}")
            print(f"Course : {course}")
            print("-" * 30)
    else:
        print("No students found.")

    connection.close()


def search_student(name):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )

    students = cursor.fetchall()

    if students:
        for student in students:
            student_id, name, age, course = student

            print("\nStudent Found")
            print(f"ID     : {student_id}")
            print(f"Name   : {name}")
            print(f"Age    : {age}")
            print(f"Course : {course}")
            print("-" * 30)
    else:
        print("Student not found.")

    connection.close()

def update_student(student_id, age, course):
        connection = sqlite3.connect("student.db")
        cursor = connection.cursor()

        sql = "UPDATE students SET age = ?, course = ? WHERE id = ?"

        values =(age, course, student_id)

        cursor.execute(sql,values)

        connection.commit()
        connection.close()  
    