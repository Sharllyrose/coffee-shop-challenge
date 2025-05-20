
# tests/coffee_test.py
import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []  # Reset orders before each test
        self.coffee = Coffee("Latte")
        self.customer = Customer("Alice")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("ab")  # Less than 3 characters
        with self.assertRaises(ValueError):
            Coffee(123)   # Not a string
        self.assertEqual(self.coffee.name, "Latte")

    def test_name_immutability(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Mocha"  # Should raise since no setter exists

    def test_orders(self):
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertEqual(self.coffee.orders()[0].price, 5.0)
        customer2 = Customer("Bob")
        Order(customer2, self.coffee, 4.5)
        self.assertEqual(len(self.coffee.orders()), 2)

    def test_customers(self):
        self.assertEqual(self.coffee.customers(), [self.customer])
        customer2 = Customer("Bob")
        Order(customer2, self.coffee, 4.5)
        self.assertEqual(set(customer.name for customer in self.coffee.customers()), {"Alice", "Bob"})

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 1)
        customer2 = Customer("Bob")
        Order(customer2, self.coffee, 4.5)
        self.assertEqual(self.coffee.num_orders(), 2)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 5.0)
        customer2 = Customer("Bob")
        Order(customer2, self.coffee, 4.0)
        self.assertEqual(self.coffee.average_price(), 4.5)  # (5.0 + 4.0) / 2
        coffee2 = Coffee("Espresso")
        self.assertEqual(coffee2.average_price(), 0)  # No orders

if __name__ == "__main__":
    unittest.main()