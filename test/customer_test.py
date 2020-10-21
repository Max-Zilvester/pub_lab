import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
 
  def setUp(self):
        self.customer = Customer("Joe Bloggs", 10.00)

    # def test_pub_has_name(self):
    #     self.assertEqual("The Prancing Pony", self.pub.name)