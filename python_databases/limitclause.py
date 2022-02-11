#https://www.geeksforgeeks.org/python-sqlite-limit-clause/
#https://www.geeksforgeeks.org/python-sqlite-join-clause/
import sqlite3

connection = sqlite3.connect('insertdata.db')
cursor = connection.cursor()


cursor.execute('''DROP TABLE IF EXISTS STUDENT''')

table_command = """
CREATE TABLE STUDENT(
NAME TEXT,
CLASS VARCHAR(255),
AGE INTEGER
);"""

cursor.execute(table_command)
data_tuples = [
('Bob', 'English', 22),
('April', 'Algebra', 19),
('Sammy', 'History', 21),
('Bill', 'Geometry', 20),
('Smith', 'Algebra', 19),
('Charles', 'English', 18),
('Andy', 'History', 20),
('Cindy', 'Geometry', 22),
("Elle", 'English', 18),
("Faith", 'English', 23)
]

if cursor:
    print("Database Created!")
else:
    print('Database Creation Failed')

insert_command = '''INSERT INTO STUDENT (NAME, CLASS, AGE) VALUES (?, ?, ?);'''
for i in data_tuples:
    cursor.execute(insert_command, i)

data = cursor.execute('''SELECT * FROM STUDENT''')
print("Not sorted")
for row in data:
    print(row)
print("")

# using limit
cursor.execute("SELECT * FROM STUDENT LIMIT 4")
for row in cursor.fetchall():
    print(row)

#using JOIN





connection.commit()
connection.close()
