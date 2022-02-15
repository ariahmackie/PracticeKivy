#https://www.geeksforgeeks.org/python-sqlite-deleting-data-in-table/

import sqlite3

connection = sqlite3.connect('delete.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS STUDENT')


student_table = '''
CREATE TABLE STUDENT (
EMAIL VARCHAR(255) NOT NULL,
NAME CHAR(25) NOT NULL,
CLASS TEXT
);'''

insert = '''
INSERT INTO STUDENT (EMAIL, NAME, CLASS) VALUES (?, ?, ?);'''


student_tuples = [
('bob@gmail.com', 'Bob', 'Art'),
('sam@gmail.com', 'sam', 'Art'),
('pam@gmail.com', 'pam', 'Dance'),
('sue@gmail.com', 'sue', 'Dance'),
('ami@gmail.com', 'Ami', 'Math'),
('mini@gmail.com', 'Miny', 'Math')]


# execute
cursor.execute(student_table)

for i in student_tuples:
    cursor.execute(insert, i)

print("before deleting")

cursor.execute('SELECT * FROM STUDENT')
result = cursor.fetchall()
for row in result:
    print(row)

# delete
print("delete art students")
cursor.execute("DELETE FROM STUDENT WHERE CLASS = 'Art'")
print('after deleting')
cursor.execute('SELECT * FROM STUDENT')
result = cursor.fetchall()
for row in result:
    print(row)

#delete all data
print("Delete everything")
cursor.execute("DELETE FROM STUDENT")
cursor.execute(" SELECT * FROM STUDENT")
result = cursor.fetchall()
for row in result:
    print(row)





connection.commit()
connection.close()
