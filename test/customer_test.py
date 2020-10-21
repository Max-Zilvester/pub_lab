import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Joe Bloggs", 34, 10.00, 0)
        self.drink = Drink("Budweiser", 3.75, 4) 

    def test_customer_has_name(self):
        self.assertEqual("Joe Bloggs", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_buy_a_drink(self):
        self.customer.buy_a_drink(self.drink)
        self.assertEqual(6.25, self.customer.wallet)

    def test_customer_has_drunkeness_level(self):
        self.assertEqual(0, self.customer.drunkeness_level)

    def test_increase_alcohol_level(self):
        self.customer.increase_alcohol_level(self.drink)
        self.assertEqual(4, self.customer.drunkeness_level)
        
