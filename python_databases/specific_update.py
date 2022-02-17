# https://www.geeksforgeeks.org/python-sqlite-update-specific-column/
import sqlite3

connection = sqlite3.connect('abc.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS STUDENTS")
cursor.execute('''CREATE TABLE STUDENTS(
ID INTEGER PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INTEGER NOT NULL,
ADDRESS CHAR(50));''')

insert = "INSERT INTO STUDENTS (ID, NAME, AGE, ADDRESS) VALUES (?, ?, ?, ?)"
student_tuples = [
(1, "Amy", 12, "1st street"),
(2, "Bailey", 10, "3rd street"),
(3, "cidney", 11, "alpha ave")
]
for i in student_tuples:
    cursor.execute(insert, i)

cursor.execute('SELECT * FROM STUDENTS')
for row in cursor:
    print(row)

cursor.execute("UPDATE STUDENTS SET NAME = 'Bill' WHERE ID = 3")

result = cursor.execute("SELECT * FROM STUDENTS")
for row in result:
    print(row)
cursor = connection.cursor()
cursor.execute("UPDATE STUDENTS SET ADDRESS = 'nag' WHERE AGE = 12")

cursor = connection.execute('SELECT * FROM STUDENTS')
for row in cursor:
    print(row)
