import sqlite3
import random

class DatabaseConnection:
    def __init__(self):
        self.connection = sqlite3.connect("rpg_data.db")
        self.cursor = self.connection.cursor()
        print("Connected to rpg_data.db")
        self.drop_all_tables()
        self.cursor.close()
        self.connection.close()

    def get_all_tables(self):
        command = "SELECT name FROM sqlite_schema WHERE type = 'table';"
        self.cursor.execute(command)
        tables = self.cursor.fetchall()
        return tables

    def drop_all_tables(self):
        tables = self.get_all_tables()
        for table_name in tables:
            command = 'DROP TABLE IF EXISTS %s' % table_name
            self.cursor.execute(command)
        print("Dropped all tables")


class PlayerTable(DatabaseConnection):
    def __init__(self):
        super(PlayerTable, self).__init__( )
        self.connection = sqlite3.connect("rpg_data.db")
        self.cursor = self.connection.cursor()
        self.create_player_table()

    def create_player_table(self):
        self.cursor.execute('''CREATE TABLE Player(
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        isloggedin INTEGER NOT NULL,
        level INTEGER NOT NULL,
        coins INTEGER NOT NULL,
        experience INTEGER NOT NULL,
        health INTEGER NOT NULL,
        strength INTEGER NOT NULL,
        perception INTEGER NOT NULL,
        intelligence INTEGER NOT NULL,
        charisma INTEGER NOT NULL,
        image BLOB);''')
        print("Created player table")

    def add_new_player(self, email, username, password):
        command = "INSERT INTO Player (email, username, password, isloggedin, level, coins, experience, health, strength, perception, intelligence, charisma) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
        player_tuple = (email, username, password, 1, 1, 100, 0, 100, 0, 0, 0, 0)
        self.cursor.execute(command, player_tuple)
        print("added new player")

    def return_first_player(self):
        self.cursor.execute("SELECT * FROM Player")
        first_player = self.cursor.fetchone()
        return first_player

    def get_value_from_player(self, value_type, player_id):
        command = "SELECT %s FROM Player WHERE id=?" % value_type
        self.cursor.execute(command, (player_id,))
        value = self.cursor.fetchone()[0]
        return value

    def print_player_table(self):
        print("Player Table")
        player_tuple = ("id", 'email', "username", "password", "isloggedin", "level", "coins", "experience", "strength", "perception", "intelligence", "charisma", "image")
        print(player_tuple)
        data = self.cursor.execute("SELECT * From Player")
        for i in data:
            print(i)
        print("")


class InventoryTable(DatabaseConnection):
    def __init__(self):
        pass

class StockTable(DatabaseConnection):
    def __init__(self):
        pass

class TaskTable(DatabaseConnection):
    def __init__(self):
        pass
