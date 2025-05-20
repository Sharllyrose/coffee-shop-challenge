
# tests/order_test.py
import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []  # Reset orders before each test
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_initializer_validation(self):
        with self.assertRaises(TypeError):
            Order("not a customer", self.coffee, 5.0)  # Invalid customer
        with self.assertRaises(TypeError):
            Order(self.customer, "not a coffee", 5.0)  # Invalid coffee
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # Price below range
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # Price above range
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5.0")  # Price not a float
        self.assertEqual(self.order.price, 5.0)

    def test_price_immutability(self):
        with self.assertRaises(AttributeError):
            self.order.price = 6.0  # Should raise since no setter exists

    def test_customer_property(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.customer.name, "Alice")

    def test_coffee_property(self):
        self.assertEqual(self.order.coffee, self.coffee)
        self.assertEqual(self.order.coffee.name, "Latte")

if __name__ == "__main__":
    unittest.main()