import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Budweiser", 3.75, 4)
        self.drink2 = Drink("White Wine", 4.50, 11)
        self.drink3 = Drink("Red Wine", 4.50, 11)
        self.drink4 = Drink("Coke", 2.50, 0)
        

    def test_drink_has_name(self):
        self.assertEqual("Budweiser", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.75, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(4, self.drink.alcohol_level)