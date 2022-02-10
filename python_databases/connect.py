# https://www.geeksforgeeks.org/python-sqlite-connecting-to-database/

import sqlite3
try:
	connection = sqlite3.connect("mydatabase.db")
	#use cursor to execute queries

	cursor = connection.cursor()
	print("DB Init")

	# the query
	query = 'select sqlite_version();'
	cursor.execute(query)

	# the result
	result = cursor.fetchall()
	print('SQLite version is {}'.format(result))


	# close 
	cursor.close

# handle error 
except sqlite3.Error as error:
	print('Error - ', error)

finally:
	if connection:
		connection.close()
		print('Connection Closed')
