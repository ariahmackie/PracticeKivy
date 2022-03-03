'''Create Database for All Classes in RPG Game'''
import sqlite3

connection =sqlite3.connect("rpg_data.db")
cursor = connection.cursor()

#Tuples
# (level, coins, experience, strength, perception, intelligence, charisma)

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
("enchilada", "any", 3),
("sandwich", "any", 2)
]

# PLAYER TABLE------------------------------------------------------------------
def create_player_table():
    cursor.execute('''CREATE TABLE Player(
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    isloggedin INTEGER NOT NULL,
    level INTEGER NOT NULL,
    coins INTEGER NOT NULL,
    experience INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    perception INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    charisma INTEGER NOT NULL,
    image BLOB);''')

def add_new_player(email, username, password):
    command = "INSERT INTO Player (email, username, password, isloggedin, level, coins, experience, strength, perception, intelligence, charisma) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
    player_tuple = (email, username, password, 1, 1, 100, 0, 0, 0, 0, 0)
    cursor.execute(command, player_tuple)

def get_xp(player_id):
    player_id = (player_id,)
    command = "SELECT experience WHERE id=?"
    cursor.execute(command, player_id)
    experience = cursor.fetchone()[0]
    return experience

def increase_xp(player_id, value):
    prior_experience = get_xp(player_id)
    experience = prior_experience + value
    xp_tuple = (experience, player_id)
    command = "UPDATE PLAYER SET experience=? WHERE id=?"
    cursor.execute(command, xp_tuple)


def drop_player_table():
    cursor.execute('DROP TABLE IF EXISTS Player')

def print_player_table():
    print("Player Table")
    player_tuple = ("id", 'email', "username", "password", "isloggedin", "level", "coins", "experience", "strength", "perception", "intelligence", "charisma", "image")
    print(player_tuple)
    data = cursor.execute("SELECT * From Player")
    for i in data:
        print(i)
    print("")

#INVENTORY TABLE ---------------------------------------------------------------
def create_inventory_table():
    cursor.execute('''CREATE TABLE Inventory(
    id INTEGER NOT NULL PRIMARY KEY,
    count INTEGER NOT NULL,
    item_id INTEGER NOT NULL);''')

def drop_inventory_table():
    cursor.execute('DROP TABLE IF EXISTS Inventory')

def populate_inventory_table():
    cursor.execute()
#ITEM TABLE--------------------------------------------------------------------
def create_item_table():
    cursor.execute('''CREATE TABLE Item(
    id INTEGER NOT NULL PRIMARY KEY,
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
    print("")

def drop_item_table():
    cursor.execute('DROP TABLE IF EXISTS Item')

# TASK TABLE ---------------------------------------
def create_task_table():
    cursor.execute('''CREATE TABLE Tasks(
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    duedate TEXT,
    value INTEGER NOT NULL,
    is_repeatable INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    complete INTEGER NOT NULL,
    FOREIGN KEY(person_id) REFERENCES Player(id));''')

def drop_task_table():
    cursor.execute('DROP TABLE IF EXISTS Tasks')

def create_task(description, duedate, value, is_repeatable, person_id):
    command = "INSERT INTO Tasks (description, duedate, value, is_repeatable, person_id, complete) VALUES (?, ?, ?, ?, ?, ?)"
    task_tuple = (description, duedate, value, is_repeatable, person_id, 0)
    cursor.execute(command, task_tuple)

def delete_task(task_id):
    task_id = (task_id,)
    command = "DELETE FROM Tasks WHERE id=?"
    cursor.execute(command, task_id)

def complete_task(task_id):
    task_id = (task_id,)
    command = "UPDATE Tasks SET complete = 1 WHERE id=?"
    cursor.execute(command, task_id)
    cursor.execute("SELECT value FROM Tasks WHERE id=?", task_id)
    value = cursor.fetchone()[0]

def get_player_id_from_task(task_id):
    pass


def print_task_table():
    task_tuple = ("id", "description", "duedate", "value", "is_repeatable", "person_id", "complete")
    print(task_tuple)
    data = cursor.execute("SELECT * FROM Tasks")
    for i in data:
        print(i)
    print('')

drop_player_table()
drop_inventory_table()
drop_task_table()
drop_item_table()

create_item_table()
create_inventory_table()
create_task_table()
create_player_table()

add_new_player("adam@gmail.com", "adam", "abc123")
create_task("walk the dog", "3-4-2021", 10, 0, 1)
print("before completing task")
print_player_table()
complete_task(1)
