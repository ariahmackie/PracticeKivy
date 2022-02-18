#https://www.sqlitetutorial.net/sqlite-foreign-key/
import sqlite3
print(sqlite3.version)
connection = sqlite3.connect("foreign_key.db")
cursor = connection.cursor()
data = cursor.execute('PRAGMA foreign_keys = ON;')
#DROP TABLES
cursor.execute('DROP TABLE IF EXISTS CLASS')
cursor.execute('DROP TABLE IF EXISTS STUDENTS')

#CREATE TABLES
cursor.execute('''CREATE TABLE CLASS(
CLASS_ID INTEGER PRIMARY KEY,
CLASS_NAME TEXT NOT NULL);''')

cursor.execute('''CREATE TABLE STUDENTS(
STUDENT_ID INTEGER PRIMARY KEY,
STUDENT_NAME TEXT NOT NULL,
CLASS_ID INTEGER NOT NULL,
FOREIGN KEY (CLASS_ID)
    REFERENCES CLASS (CLASS_ID)
);''')

#POPULATE TABLES
cursor.execute('''INSERT INTO CLASS (CLASS_NAME)
VALUES
('ART'),
('HISTORY'),
('MATH');''')

cursor.execute('''INSERT INTO STUDENTS (STUDENT_NAME, CLASS_ID)
VALUES ('Bob', 1);''')

cursor.execute('''INSERT INTO STUDENTS (STUDENT_NAME, CLASS_ID)
VALUES ('Pam', 2);''')

cursor.execute('''INSERT INTO STUDENTS (STUDENT_NAME, CLASS_ID)
VALUES ('Sam', 3);''')

data = cursor.execute('SELECT * FROM STUDENTS ')
data2 = cursor.execute('SELECT * FROM CLASS')
print("students")
for row in data:
    print(row)

print("classes")
for row in data2:
    print(row)

connection.commit()
connection.close()
