import unittest
import rpg_database as rpg

class TestPlayerTable(unittest.TestCase):
    def setUp(self):
        rpg.drop_all_tables()

    def set_up_player(self):
        rpg.create_player_table()
        rpg.add_new_player("adm@gmail.com", "Adam", "1234")

    def set_up_inventory(self):
        self.set_up_player()
        rpg.create_stock_table()
        rpg.populate_stock_table()
        rpg.create_inventory_table()

    def drop_tables(self):
        rpg.drop_all_tables()

    def test_add_new_player(self):
        rpg.create_player_table()
        rpg.add_new_player("adm@gmail.com", "Adam", "1234")
        expected_tuple = (1, 'adm@gmail.com', 'Adam', '1234', 1, 1, 100, 0, 100, 0, 0, 0, 0, None)
        actual_tuple = rpg.get_player(1)
        self.assertEqual(expected_tuple, actual_tuple, "tuples should be the same")
        self.drop_tables()

    def test_get_value_from_player(self):
        self.set_up_player()
        actual_email = rpg.get_value_from_player("email", 1)
        expected_email = "adm@gmail.com"
        self.assertEqual(expected_email, actual_email, "emails should be the same")
        self.drop_tables()

    def test_change_value_in_player(self):
        self.set_up_player()
        rpg.change_value_in_player("username", "Mary", 1)
        actual_username = rpg.get_value_from_player("username", 1)
        expected_username = "Mary"
        self.assertEqual(actual_username, expected_username, "Names should be the same")
        self.drop_tables()

    def test_decrease_value_in_player(self):
        self.set_up_player()
        rpg.decrease_value_from_player("health", 2, 1)
        expected_health = 98
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should have decreased by 2")
        self.drop_tables()

    def test_increase_value_in_player(self):
        self.set_up_player()
        rpg.increase_value_in_player("strength", 2, 1)
        expected_strength = 2
        actual_strength = rpg.get_value_from_player("strength", 1)
        self.assertEqual(expected_strength, actual_strength, "strength should be raised by 2")
        self.drop_tables()

    def test_increase_health_in_player(self):
        self.set_up_player()
        rpg.increase_health(1, 5)
        expected_health = 100
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should only be 100 because it can't go past 1100")
        self.drop_tables()

    def test_decrease_health_in_player(self):
        self.set_up_player()
        rpg.decrease_health(1, 50)
        expected_health = 50
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should decrease by 50")
        rpg.decrease_health(1, 55)
        expected_health = 0
        actual_health = rpg.get_value_from_player("health", 1)
        self.assertEqual(expected_health, actual_health, "health should be 0 and not negative")
        self.drop_tables()

    def test_add_item_by_id(self):
        self.set_up_inventory()
        rpg.add_item_by_id(2, 1)
        actual_item = rpg.get_item_by_id(1)
        expected_item = (1, "banana", 1,  2, 1)
        self.assertEqual(actual_item, expected_item, "should return banana item")
        self.drop_tables()

    def test_add_item_by_name(self):
        self.set_up_inventory()
        rpg.add_item_by_name("berries", 1)
        actual_item = rpg.get_item_by_id(1)
        expected_item = (1, "berries", 1, 3, 1)
        self.assertEqual(actual_item, expected_item, "item should be berries")
        self.drop_tables()

    def test_add_item(self):
        self.set_up_inventory()
        item_tuple = (1, "cheese", 2, "meal")
        rpg.add_item(item_tuple, 1)
        actual_item = rpg.get_item_by_id(1)
        expected_item = (1, "cheese", 1, 1, 1)
        self.assertEqual(actual_item, expected_item, "item should be cheese")
        self.drop_tables()

    def test_count_how_many_of_item(self):
        self.set_up_inventory()
        rpg.add_item_by_id(1, 1)
        actual_count = rpg.count_how_many_of_item("apple", 1)
        expected_count = 1
        self.assertEqual(actual_count, expected_count, "count should be 1")
        self.drop_tables()



if __name__ == "__main__":
    unittest.main()