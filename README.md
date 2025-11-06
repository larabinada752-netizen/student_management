# Student Management System

This is a small project I built using Python and MySQL.
The goal is to manage students in an easy and fast way: I can add, view, update, and delete students directly from the database.
Everything runs from the Terminal or VS Code terminal, and I tried it myself.

---

##  Features

- Add new students with `name` and `age`.  
- View all students in the database.  
- Update student information by `ID`.  
- Delete students by `ID`.  
- Works directly with MySQL database.  
- Console-based menu for easy navigation.  

---

##  Prerequisites

- Python 3.x installed
- MySQL server installed and running
- `mysql-connector-python` library installed:

  bash
pip install mysql-connector-python
A MySQL database named students_db (or modify database.py to match your DB name)

A table named students with columns:

id INT AUTO_INCREMENT PRIMARY KEY

name VARCHAR(100)

age INT

## Getting Started
### 1 Clone this repository:

bash
Copier le code
git clone https://github.com/username/student_management.git
cd student_management
### 2 Install dependencies:

bash
Copier le code
pip install mysql-connector-python
### 3 Make sure your MySQL server is running.

### 4 Open database.py and ensure the connection settings match your database:

python
Copier le code
host="localhost"
user="root"
password=""          # Your MySQL password
database="students_db"
### 5 Run the main program:

bash
Copier le code
python main.py
### 6 Use the menu to manage students:

pgsql
Copier le code
===== Student Management System =====
1. Add Student
2. Show All Students
3. Update Student Data
4. Delete Student
5. Exit
## Screenshots
### 1 Running the program in Terminal:


### 2 Viewing the table in phpMyAdmin:


Make sure to create a folder named screenshots and add your captured images there.

## Project Structure
css
Copier le code
student_management/
│─ main.py
│─ database.py
│─ README.md
│─ screenshots/
│   ├─ terminal.png
│   └─ phpmyadmin.png
│─ __pycache__/  (ignored in .gitignore)
## How It Works
database.py handles all database operations: connect, create table, add, show, update, delete students.

main.py provides a menu-driven interface for the user.

Each action in the menu interacts directly with MySQL.

## Notes
Do not include sensitive information (like passwords) in your GitHub repository.

The project can be extended by adding features like search by name, filtering by age, or GUI interface.


