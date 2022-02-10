import sqlite3

connection = sqlite3.connect('cursor.db')

connection.execute('''DROP TABLE player;''')


connection.execute('''CREATE TABLE player(
USERID INTEGER NOT NULL PRIMARY KEY,
USERNAME TEXT NOT NULL,
EMAIL TEXT,
COINS INTEGER,
IMAGE BLOB);''')

cursor = connection.cursor()
photo_file = open('dolphin.png', "rb")
binary_photo = photo_file.read()
photo_tuple = ("IMAGE", binary_photo)
insertquery = '''INSERT INTO player (USERNAME, EMAIL, COINS) VALUES ('Dolphin', 'dolphin@gmail.com', 212);'''
cursor.execute(insertquery)


#connection.commit()


query  = connection.execute('''SELECT * FROM player;''')
for i in query:
        print("ID: " + str(i[0]) + "USERNAME: " + str(i[1]) + " EMAIL: " + str(i[2]) + " COINS: " + str(i[3]) )
	
