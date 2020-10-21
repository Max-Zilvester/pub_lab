import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Joe Bloggs", 34, 10.00, 0)
        self.customer_2 = Customer("Bob Smith", 17, 5.00, 0)
        self.customer_3 = Customer("Bob Dylan", 55, 30.00, 15)
        self.drink = Drink("Budweiser", 3.75, 4) 
        self.food = Food("Lasagne", 2.50, 5)

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
        
    def test_reduce_drunkeness_level(self):
        self.customer_3.reduce_drunkeness_level(self.food)
        self.assertEqual(10, self.customer_3.drunkeness_level)
