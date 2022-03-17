import unittest
import rpg_database_class as rpg
import sqlite3

class TestPlayerTable(unittest.TestCase):
    def setUp(self):
        self.player_table = rpg.PlayerTable()

    def test_add_new_player(self):
        self.player_table.add_new_player("adam@gmail.com", "adam", "abc123")
        expected_tuple = (1, "adam@gmail.com", "adam", "abc123", 1, 1, 100, 0, 100, 0, 0, 0, 0, None)
        actual_tuple = self.player_table.return_first_player()
        self.assertEqual(expected_tuple, actual_tuple, "tuples should be the same")
        

if __name__ == "__main__":
    unittest.main()
