import sqlite3

connection = sqlite3.connect("relationship.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = 1;")
X = cursor.execute("PRAGMA foreign_keys")
print(X.fetchall())

cursor.execute("DROP TABLE IF EXISTS Albums")
cursor.execute("DROP TABLE IF EXISTS Artists")

cursor.execute('''CREATE TABLE Artists(
ArtistId INTEGER PRIMARY KEY,
ArtistName TEXT NOT NULL);''')


cursor.execute('''INSERT INTO Artists VALUES (NULL, 'Bob');''')
cursor.execute('''INSERT INTO Artists VALUES (NULL, 'Cathy');''')
cursor.execute('''INSERT INTO Artists VALUES (NULL, 'Allison');''')

cursor.execute('''CREATE TABLE Albums(
AlbumId INTEGER PRIMARY KEY,
AlbumName TEXT NOT NULL,
Year TEXT NOT NULL,
ArtistId Integer NOT NULL,
FOREIGN KEY(ArtistId) REFERENCES Artists(ArtistsId))''')

#cursor.execute('''INSERT INTO Albums (AlbumId, AlbumName, Year) VALUES (NULL, 'Bob album', 1981 );''')
#cursor.execute('''INSERT INTO Albums VALUES (NULL, 'Cathy album', 1972 );''')
#cursor.execute('''INSERT INTO Albums VALUES (NULL, 'Allison album', 1989);''')

tables = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
print(tables.fetchall())

#cursor.execute("INSERT INTO Albums (AlbumName, Year, ArtistId ) VALUES ('Poww', '1984', 70)")

artist_table = cursor.execute("SELECT * FROM Artists")
print( "Artist Table")
print(artist_table.fetchall())

albums_table = cursor.execute("SELECT * FROM Albums")
print("Album Table")
print(albums_table.fetchall())
