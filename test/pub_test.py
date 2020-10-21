import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, ["Budweiser", "White Wine", "Red Wine", "Coke"])

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual((100), self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(4, len(self.pub.drinks))
