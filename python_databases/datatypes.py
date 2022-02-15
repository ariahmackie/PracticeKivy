# https://www.geeksforgeeks.org/sqlite-datatypes-and-its-corresponding-python-types/
import sqlite3

connection = sqlite3.connect('mydb.db')

# delete existing table 
connection.execute('''DROP TABLE player;''')


# Build a table
connection.execute('''CREATE TABLE player(
USERNAME TEXT,
EMAIL TEXT,
COINS INTEGER,
LEVEL INTEGER);''')

# read a binary file
#image_file = open('dolphin.png')
#image = image_file.read()

# insert tuples 

connection.execute('''INSERT INTO player VALUES('bob',  'bob@gmail.com', 350, 5)''')
connection.execute('''INSERT INTO player VALUES('sam', 'sam@gmail.com', 200, 3)''')


# query the data
query  = connection.execute('''SELECT * FROM player;''')
for i in query:
	print("name: " + str(i[0]) + " email: " + str(i[1]) + " coins: " + str(i[2]) + " level: " + str(i[3]) )
