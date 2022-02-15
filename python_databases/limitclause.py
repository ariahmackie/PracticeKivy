#https://www.geeksforgeeks.org/python-sqlite-limit-clause/
#https://www.geeksforgeeks.org/python-sqlite-join-clause/
import sqlite3

connection = sqlite3.connect('insertdata.db')
cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS STUDENT''')
cursor.execute('''DROP TABLE IF EXISTS WORKER''')

student_table = """
CREATE TABLE STUDENT(
NAME TEXT,
CLASS VARCHAR(255),
AGE INTEGER,
STUDENT_ID INTEGER);"""

worker_table = """
CREATE TABLE WORKER(
NAME TEXT,
TYPE TEXT,
AGE INTEGER,
WORKER_ID INTEGER);"""

cursor.execute(student_table)
student_tuples = [
('Bob', 'English', 22, 1),
('April', 'Algebra', 19, 2) ,
('Sammy', 'History', 21, 3),
('Bill', 'Geometry', 20, 4),
('Smith', 'Algebra', 19, 5),
('Charles', 'English', 18, 6),
('Andy', 'History', 20, 7),
('Cindy', 'Geometry', 22, 8),
("Elle", 'English', 18, 9),
("Faith", 'English', 23, 10)]

cursor.execute(worker_table)
worker_tuples = [
('Bob', 'SALES', 23, 2),
('Allan', 'HR', 34, 4),
('Sam', 'MANAGEMENT', 22, 6),
('Smith', 'HR', 20, 8)]

if cursor:
    print("Database Created!")
else:
    print('Database Creation Failed')

insert_student_table = '''INSERT INTO STUDENT (NAME, CLASS, AGE, STUDENT_ID) VALUES (?, ?, ?, ?);'''
insert_worker_table = '''INSERT INTO WORKER (NAME, TYPE, AGE, WORKER_ID) VALUES (?, ?, ?, ?);'''

for i in student_tuples:
    cursor.execute(insert_student_table, i)

for i in worker_tuples:
    cursor.execute(insert_worker_table, i)


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
print("inner join")
inner_join = '''
SELECT STUDENT_ID, STUDENT.NAME FROM STUDENT
INNER JOIN WORKER
ON STUDENT.STUDENT_ID = WORKER.WORKER_ID; '''

cursor.execute(inner_join)

result = cursor.fetchall()
for row in result:
    print(row)

print("left join")
left_join = '''
SELECT STUDENT_ID, STUDENT.NAME,  STUDENT.AGE FROM STUDENT
LEFT JOIN WORKER USING (AGE);'''

cursor.execute(left_join)
result = cursor.fetchall()
for row in result:
    print(row)

#88888888888888888888888888888888888
print("full outer join")

join = '''SELECT STUDENT_ID, STUDENT.NAME, STUDENT.AGE
FROM STUDENT
LEFT JOIN WORKER
USING(AGE)
UNION ALL
SELECT WORKER.NAME, WORKER.TYPE, WORKER.AGE
FROM WORKER
LEFT JOIN STUDENT
USING(AGE); '''

cursor.execute(join)
result = cursor.fetchall()
for row in result:
    print(row)

print("cross join")
#combines all records from two tables
join = '''SELECT STUDENT_ID, STUDENT.NAME, STUDENT.AGE
FROM STUDENT
CROSS JOIN WORKER;'''

cursor.execute(join)
result = cursor.fetchall()
for row in result:
    print(row)




connection.commit()
connection.close()
