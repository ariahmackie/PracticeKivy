# https://www.geeksforgeeks.org/python-sqlite-create-table/


import sqlite3

connection = sqlite3.connect('createtable.db')

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS PET")

table_command = """CREATE TABLE PET (
TYPE TEXT,
AGE INTEGER,
LEVEL INTEGER,
IMAGE BLOB
);"""

cursor.execute(table_command)









query = cursor.execute("""SELECT * FROM  PET; """)
for i in query:
    print(i)


connection.close()
