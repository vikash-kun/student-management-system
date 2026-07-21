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

    values = (age, course, student_id)

    cursor.execute(sql,values)
    if cursor.rowcount == 0:
     print("No student found with that ID.")
    else:
        connection.commit()
        print("Student updated successfully!") 

    connection.close()  

def delete_student(student_id):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

    sql = "DELETE FROM students WHERE id = ?"
    values = (student_id,)
    cursor.execute(sql,values)
    if cursor.rowcount == 0:
        print("No student found with that ID")
    else:
        connection.commit()
        print("Student deleted successfully!")    
    connection.close()  

def sort_students():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students ORDER BY age DESC;")

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

def count_students():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor() 

    cursor.execute("SELECT COUNT(*) FROM students;")

    result = cursor.fetchone()

    print("===== Student Statistics =====")
    print("Total Students :", result[0])

    connection.close()

def search_by_age_course(age, course):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor() 

    cursor.execute("SELECT * FROM students WHERE age = ? AND course = ?",
                   (age, course))

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
def search_by_age_or_course(age, course):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT * FROM students WHERE age = ? OR course = ?",
                      (age, course))
   
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

def search_student_partial(name):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE name LIKE ?;",
                   ("%" + name + "%",)) 

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

def average_age():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()         
    cursor.execute("SELECT AVG(age) FROM students;")

    result = cursor.fetchone()

    print("===== Student Statistics =====")
    print("Average Age :",result[0] )    

    connection.close()       

def maximum_age():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()                
    cursor.execute("SELECT MAX(age) FROM students;")

    result = cursor.fetchone()

    print("===== Student Statistics =====")
    print("Maximum age:",result[0] )  

    connection.close()   

def minimum_age():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()    

    cursor.execute("SELECT MIN(age) FROM students;")

    result = cursor.fetchone()

    print("===== Student Statistics =====")
    print("Minimun age:",result[0] )  

    connection.close()   

def total_age():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()   

    cursor.execute("SELECT SUM(age) FROM students;")

    result = cursor.fetchone()

    print("===== Student Statistics =====")
    print("Total age:",result[0] )  

    connection.close()  

def unique_courses():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()      

    cursor.execute("SELECT DISTINCT course FROM students;")

    courses = cursor.fetchall()

    print("===== Available Courses =====")
    for course in courses:
        print(f"Course : {course[0]}") 
    connection.close()   

def students_by_course():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()   

    cursor.execute("SELECT course, COUNT(*) FROM students GROUP BY course;") 

    result = cursor.fetchall()

    print("===== Students by Course =====")

    for row in result:
         print(f"{row[0]:30} : {row[1]}")

    connection.close()     
