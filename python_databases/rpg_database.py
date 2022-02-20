'''Create Database for All Classes in RPG Game'''
import sqlite3

connection =sqlite3.connect("rpg_data.db")
cursor = connection.cursor()


def create_player_table():
    cursor.excute('''CREATE TABLE Player(
    tasks_id INTEGER NOT NULL,
    coins INTEGER NOT NULL,
    backpack_id INTEGER NOT NULL,
    experience INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    perception INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    charisma INTEGER NOT NULL,
    FOREIGN KEY (tasklist_id)
        REFERENCES CLASS (Tasklist),
    FOREIGN KEY (backpack_id)
        REFERENCES CLASS (Backpack));''')


def create_account_table():
    
    pass

def create_backpack_table():
    pass

def create_task_table():
    pass

def create_all_tables():
    pass

def drop_all_tables():
    pass

def drop_specific_table():
    pass
