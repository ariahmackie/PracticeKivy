'''Create Database for All Classes in RPG Game'''
import sqlite3

connection =sqlite3.connect("rpg_data.db")
cursor = connection.cursor()

#Tuples
# (level, coins, experience, strength, perception, intelligence, charisma)
player_tuples = [
(1, 120, 15, 2, 3, 4, 3),
(3, 55, 32, 3, 3, 4, 3),
(2, 72, 21, 1, 3, 4, 3),
(3, 202, 9, 8, 3, 4, 3),
(4, 130, 40, 2, 9, 4, 3)
]

account_tuples = [
("aaa@gmail.com", "Alfred","123456", 0),
("bbb@gmail.com", "Bob","123456", 0),
("ccc@gmail.com", "Cessily","123456", 0),
("ddd@gmail.com", "Danny","123456", 0),
("eeea@gmail.com", "Emma","123456", 0)
]


#description, user, health_value
food_tuples =[
("apple", "any", 2),
("banana", "any", 2),
("berries", "any", 2),
("cherries", "any", 2),
("coconut", "any", 3),
("grapefruit", "any", 2),
("grapes", "any", 2),
("kiwi", "any", 2),
("lemon", "any", 2),
("lime", "any", 2),
("mango", "any", 2),
("orange", "any", 2),
("peach", "any", 2),
("pear", "any", 2),
("pineapple", "any", 2),
("strawberries", "any", 2),
("watermelon", "any", 2)









]


# PLAYER TABLE------------------------------------------------------------------
def create_player_table():
    cursor.execute('''CREATE TABLE Player(
    player_id INTEGER NOT NULL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    tasks_id INTEGER NOT NULL,
    inventory_id INTEGER NOT NULL,
    level INTEGER NOT NULL,
    coins INTEGER NOT NULL,
    experience INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    perception INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    charisma INTEGER NOT NULL,
    image BLOB,
    FOREIGN KEY (account_id)
        REFERENCES CLASS (Account),
    FOREIGN KEY (tasks_id)
        REFERENCES CLASS (Tasks),
    FOREIGN KEY (inventory_id)
        REFERENCES CLASS (Inventory));''')

def populate_player_table():
    command = "INSERT INTO Player (level, coins, experience, strength, perception, intelligence, charisma) VALUES (?, ?, ?, ?, ?, ?, ?)"
    for i in player_tuples:
        cursor.execute(command, i)

def drop_player_table():
    cursor.execute('DROP TABLE IF EXISTS Player')

#ACCOUNT TABLE ----------------------------------------------------------------
def create_account_table():
    cursor.execute('''CREATE TABLE Account(
    account_id INTEGER NOT NULL PRIMARY KEY,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    isloggedin INTEGER NOT NULL);''')

def populate_account_table():
    pass

def drop_account_table():
    cursor.execute('DROP TABLE IF EXISTS Account')

#INVENTORY TABLE ---------------------------------------------------------------
def create_inventory_table():
    cursor.execute('''CREATE TABLE Inventory(
    inventory_id INTEGER NOT NULL PRIMARY KEY,
    count INTEGER NOT NULL,
    item_id INTEGER NOT NULL);''')

def drop_inventory_table():
    cursor.execute('DROP TABLE IF EXISTS Inventory')

#ITEM TABLE--------------------------------------------------------------------
def create_item_table():
    cursor.execute('''CREATE TABLE Item(
    item_id INTEGER NOT NULL PRIMARY KEY,
    type TEXT NOT NULL,
    description TEXT NOT NULL,
    user TEXT NOT NULL,
    image BLOB NOT NULL);''')

# TASK TABLE ---------------------------------------
def create_task_table():
    cursor.execute('''CREATE TABLE Tasks(
    tasks_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    duedate TEXT,
    value INTEGER NOT NULL,
    is_repeatable INTEGER NOT NULL);''')

def drop_task_table():
    cursor.execute('DROP TABLE IF EXISTS Tasks')

def test():
    print("hello")

test()
drop_player_table()
drop_account_table()
drop_inventory_table()
drop_task_table()

create_account_table()
create_inventory_table()
create_task_table()
create_player_table()
