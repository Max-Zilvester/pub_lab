import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
     
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, ["Budweiser", "White Wine", "Red Wine", "Coke"])
        self.drink = Drink("Budweiser", 3.75, 4)
        self.customer = Customer("Joe Bloggs", 34, 10.00, 0)
        self.customer_2 = Customer("Bob Smith", 17, 5.00, 0)
        self.customer_3 = Customer("Bob Dylan", 55, 30.00, 15)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual((100), self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(4, len(self.pub.drinks))

    def test_sell_a_drink(self):
        self.pub.sell_a_drink(self.drink, self.customer)
        self.assertEqual(103.75, self.pub.till)

    def test_sell_a_drink__check_age(self):
        self.pub.sell_a_drink(self.drink, self.customer_2)
        self.assertEqual(100.00, self.pub.till)
        
    def test_sell_a_drink__check_drunkeness(self):
        self.pub.sell_a_drink(self.drink, self.customer_3)
        self.assertEqual(100.00, self.pub.till)

