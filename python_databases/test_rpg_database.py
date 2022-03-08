import unittest
import rpg_database as rpg
import sqlite3

connection =sqlite3.connect("rpg_data.db")
cursor = connection.cursor()
#make databasetable

rpg.drop_all_tables()
rpg.create_all_tables()
cursor.execute("SELECT name FROM sqlite_master WHERE type ='table';")
print(cursor.fetchall())

class TestPlayerTable(unittest.TestCase):

    def test_add_new_player(self):
        rpg.add_new_player("Frodo@gmail.com", "Frodo", "abc123")
        correct_tuple =  ("Frodo@gmail.com", "Frodo", "abc123", 1, 1, 100, 0, 100, 0, 0, 0, 0)
        data = cursor.execute("SELECT * FROM Player")
        for i in data:
            print(i)
        #actual_tuple = cursor.fetchone()
        #print(correct_tuple)
        #print(actual_tuple)
        #self.assertEqual(correct_tuple, actual_tuple, "tuples should match")

if __name__ == "__main__":
    unittest.main()
