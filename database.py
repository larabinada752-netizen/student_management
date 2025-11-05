import mysql.connector

# Connect to the database
def connect():
    print("Trying to connect to the database...")  # رسالة قبل الاتصال
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         # Username in phpMyAdmin
        password="",         # Leave empty if no password
        database="students_db"  # Same name as in phpMyAdmin
    )
    print("Connection successful!")  # رسالة إذا الاتصال نجح
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, age):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    conn.close()
    print("Student added successfully!")

def show_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\nList of Students:")
    for s in students:
        print(f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}")
    conn.close()

def update_student(student_id, new_name, new_age):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s WHERE id=%s", (new_name, new_age, student_id))
    conn.commit()
    conn.close()
    print("Student data updated successfully!")

def delete_student(student_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")
