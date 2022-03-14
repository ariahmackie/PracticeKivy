import unittest
import rpg_database as rpg

class TestPlayerTable(unittest.TestCase):
    def setUp(self):
        rpg.drop_all_tables()

    def test_add_new_player(self):
        rpg.create_player_table()
        rpg.add_new_player('adm@gmail.com', 'Adam', "1234")
        expected_tuple = (1, 'adm@gmail.com', 'Adam', '1234', 1, 1, 100, 0, 100, 0, 0, 0, 0, None)
        actual_tuple = rpg.get_player(1)
        self.assertEqual(expected_tuple, actual_tuple, "tuples should be the same")
        rpg.drop_all_tables()

    def test_get_value_from_player(self):
        rpg.create_player_table()
        rpg.add_new_player("a@gmail.com", "Ashley", "1234")
        actual_email = rpg.get_value_from_player("email", 1)
        expected_email = "a@gmail.com"
        self.assertEqual(expected_email, actual_email, "emails should be the same")

    

if __name__ == "__main__":
    unittest.main()
