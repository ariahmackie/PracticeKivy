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

insertquery = '''INSERT INTO player (USERID, USERNAME, EMAIL, COINS, IMAGE) VALUES (?, ?, ?, ?, ?);'''

data_tuple = (1, "bob", "bob@gmail.com", 5, binary_photo)
cursor.execute(insertquery, data_tuple)


#connection.commit()


query  = connection.execute('''SELECT * FROM player;''')
for i in query:
    print(i[0:3])
