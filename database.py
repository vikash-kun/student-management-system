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

def insert_student(name,age,course):
    connection= sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    (name, age, course)
)

    connection.commit()
    connection.close()