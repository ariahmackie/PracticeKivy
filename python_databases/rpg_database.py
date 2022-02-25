'''Create Database for All Classes in RPG Game'''
import sqlite3

connection =sqlite3.connect("rpg_data.db")
cursor = connection.cursor()

#Tuples
# (level, coins, experience, strength, perception, intelligence, charisma)
player_tuples = [
(NULL, NULL, NULL, NULL, 1, 120, 15, 2, 3, 4, 3),
(NULL, NULL, NULL, NULL, 3, 55, 32, 3, 3, 4, 3),
(NULL, NULL, NULL, NULL, 2, 72, 21, 1, 3, 4, 3),
(NULL, NULL, NULL, NULL, 3, 202, 9, 8, 3, 4, 3),
(NULL, NULL, NULL, NULL, 4, 130, 40, 2, 9, 4, 3)
]

account_tuples = [
("aaa@gmail.com", "Alfred","123456", 0),
("bbb@gmail.com", "Bob","123456", 0),
("ccc@gmail.com", "Cessily","123456", 0),
("ddd@gmail.com", "Danny","123456", 0),
("eeea@gmail.com", "Emma","123456", 0)
]


#description, user, health_value
fruit_tuples =[
("apple", "any", 2),
("banana", "any", 3),
("berries", "any", 1),
("cherries", "any", 2),
("coconut", "any", 3),
("grapefruit", "any", 4),
("grapes", "any", 1),
("kiwi", "any", 2),
("lemon", "any", 3),
("lime", "any", 4),
("mango", "any", 1),
("orange", "any", 2),
("peach", "any", 3),
("pear", "any", 4),
("pineapple", "any", 1),
("strawberries", "any", 2),
("watermelon", "any", 3)]

vegetable_tuples = [
("artichoke", "any", 1),
("asparagus", "any", 2),
("broccoli", "any" , 3),
("cabbage", "any", 4),
("carrot", "any", 1),
("cauliflower", "any", 2),
("corn", "any", 3),
("cucumber", "any", 4),
("eggplant", "any", 1),
("lettuce", "any", 2),
("mushrooms", "any", 3),
("onion", "any", 4),
("peas", "any", 1),
("potato", "any", 4),
("radishes", "any", 2),
("tomato", "any", 3)]

dessert_tuples = [
("chocolate chip cookies", "any", 3),
("apple pie", "any", 2),
("cheese cake", "any", 1),
("carrot cake", "any", 3),
("icecream", "any", 2),
("birthday cake", "any", 3),
("cotton candy", "any", 2),
("brownies", "any", 2),
("pumpkin pie", "any", 3),
("red velvet cake", "any", 2),
("donut", "any", 2),
("lollypop", "any", 1),
("cherry pie", "any", 2)]

meal_tuples = [
("ramen", "any", 1),
("sushi", "any", 1),
("chow mein", "any", 2),
("orange chicken", "any", 4),
("roast chicken", "any", 2),
("rice", "any", 3),
("taco", "any", 4),
("roast beef", "any", 3),
("baked potato", "any", 2),
("enchilado", "any", 3),
("sandwich", "any", 2)
]

# PLAYER TABLE------------------------------------------------------------------
def create_player_table():
    cursor.execute('''CREATE TABLE Player(
    player_id INTEGER PRIMARY KEY,
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
    FOREIGN KEY (account_id)REFERENCES Account (account_id),
    FOREIGN KEY (tasks_id) REFERENCES Tasks (task_id),
    FOREIGN KEY (inventory_id) REFERENCES Inventory (inventory_id));''')

def populate_player_table():
    command = "INSERT INTO Player ( player_id, account_id, tasks_id, inventory_id, level, coins, experience, strength, perception, intelligence, charisma) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    for i in player_tuples:
        cursor.execute(command, i)

def drop_player_table():
    cursor.execute('DROP TABLE IF EXISTS Player')

def print_player_table():
    print("Player Table")
    data = cursor.execute("SELECT * From Player")
    for i in data:
        print(i)

#ACCOUNT TABLE ----------------------------------------------------------------
def create_account_table():
    cursor.execute('''CREATE TABLE Account(
    account_id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    isloggedin INTEGER NOT NULL);''')

def populate_account_table():
    command = "INSERT INTO Account (email, username, password, isloggedin) VALUES (?, ?, ?, ?)"
    for i in account_tuples:
        cursor.execute(command, i)

def print_account_table():
    print("Account table")
    data = cursor.execute( "SELECT * FROM Account")
    for i in data:
        print(i)

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

def populate_inventory_table():
    cursor.execute()
#ITEM TABLE--------------------------------------------------------------------
def create_item_table():
    cursor.execute('''CREATE TABLE Item(
    item_id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    user TEXT NOT NULL,
    value INTEGER NOT NULL,
    image BLOB);''')

def populate_item_table():
    command = "INSERT INTO Item (name, user, value) VALUES (?, ?, ?)"
    for i in fruit_tuples:
        cursor.execute(command, i)

    for i in vegetable_tuples:
        cursor.execute(command, i)

    for i in dessert_tuples:
        cursor.execute(command, i)

    for i in meal_tuples:
        cursor.execute(command, i)

def print_item_table():
    data = cursor.execute("SELECT * FROM Item")
    for i in data:
        print(i)
def drop_item_table():
    cursor.execute('DROP TABLE IF EXISTS Item')

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
drop_item_table()

create_item_table()
create_account_table()
create_inventory_table()
create_task_table()
create_player_table()

populate_item_table()
populate_account_table()
populate_player_table()

print_player_table()
print_account_table()
