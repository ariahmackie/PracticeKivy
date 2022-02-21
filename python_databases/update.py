#https://www.geeksforgeeks.org/python-sqlite-update-data/
import sqlite3

connection = sqlite3.connect('update.db')

cursor = connection.cursor()
cursor.execute('''DROP TABLE IF EXISTS EMPLOYEE;''')

table = '''
CREATE TABLE EMPLOYEE(
FIRST_NAME VARCHAR(255),
LAST_NAME VARCHAR(255),
AGE INTEGER,
SEX VARCHAR(255),
INCOME INTEGER
);'''

cursor.execute(table)

employee_tuples = [
("Ally", "Smith", 29, "F", 120000),
("Benjamin", "Button", 28, "M", 50000),
("Courtney", "Cotton", 22, "F", 70000),
("Diana", "Dylan", 40, "F", 100000),
("Elle", "Effington", 32, "F", 60000)
]

command = '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (?, ?, ?, ?, ?)'''

for i in employee_tuples:
    cursor.execute(command, i)

print("Employee Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)

print("Update Income")
cursor.execute('''UPDATE EMPLOYEE SET INCOME = 100 WHERE AGE > 30;''')
print("Employee Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)

print("Update Age")
cursor.execute('''UPDATE EMPLOYEE SET AGE = 0 WHERE SEX = 'F';''')
print("Employee Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)

print("update specific")
cursor.execute('''UPDATE EMPLOYEE SET FIRST_NAME = 'Ram', AGE = 30 WHERE LAST_NAME = "Smith";''')
print("Employee Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)

print("update all ages to 30")
cursor.execute('''UPDATE EMPLOYEE SET AGE = 30;''')
print("Employee Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)





connection.commit()
connection.close()
