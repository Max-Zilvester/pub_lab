import unittest
from src.food import Food
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food = Food("Lasagne", 2.50, 5)
        self.pub = Pub("The Prancing Pony", 100.00, ["Budweiser", "White Wine", "Red Wine", "Coke"])
        self.drink = Drink("Budweiser", 3.75, 4)
        self.customer = Customer("Joe Bloggs", 34, 10.00, 0)
        self.customer_2 = Customer("Bob Smith", 17, 5.00, 0)
        self.customer_3 = Customer("Bob Dylan", 55, 30.00, 15)

    def test_food_has_name(self):
        self.assertEqual("Lasagne", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(2.50, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food.rejuvenation_level)
