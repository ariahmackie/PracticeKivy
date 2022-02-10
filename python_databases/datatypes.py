# https://www.geeksforgeeks.org/sqlite-datatypes-and-its-corresponding-python-types/
import sqlite3

connection = sqlite3.connect('mydb.db')

# delete existing table 
connection = sqlite3.connect('''DROP TABLE [IF EXISTS] player''')




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
