# https://www.geeksforgeeks.org/python-sqlite-insert-data/
#https://www.geeksforgeeks.org/python-sqlite-order-by-clause/
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
for row in data:
    print(row)

output = cursor.fetchall()
for row in output:
    print(row)

print("Where selection")

# select by age
cursor.execute('SELECT * FROM STUDENT WHERE AGE = 19')
print(cursor.fetchall())
print("")

# select by class
cursor.execute('SELECT * FROM STUDENT WHERE CLASS = "English"')
print(cursor.fetchall())
print("")
# select if NAme starts with A
cursor.execute('SELECT * FROM STUDENT WHERE NAME Like "A%" ')
print(cursor.fetchall())
print("")

#SELECT if NAME ends with B
cursor.execute('SELECT * FROM STUDENT WHERE NAME Like "%b" ')
print(cursor.fetchall())
print("")

#update a value
cursor.execute('UPDATE STUDENT SET CLASS = "English" WHERE AGE = 20')
cursor.execute('SELECT * FROM STUDENT ')
print(cursor.fetchall())
print("")

#delete a row
cursor.execute('DELETE from STUDENT WHERE AGE = 20')
cursor.execute('SELECT * FROM STUDENT')
print(cursor.fetchall())
print("")

#display descending order by age
cursor.execute('SELECT * FROM STUDENT ORDER BY AGE DESC')
print(cursor.fetchall())
print("")






connection.commit()
connection.close()
