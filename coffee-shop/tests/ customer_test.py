
# tests/customer_test.py
import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []  # Reset orders before each test
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Customer(123)
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")

    def test_orders(self):
        self.assertEqual(len(self.customer.orders()), 1)
        self.assertEqual(self.customer.orders()[0].price, 5.0)

    def test_coffees(self):
        self.assertEqual(self.customer.coffees(), [self.coffee])
        coffee2 = Coffee("Espresso")
        Order(self.customer, coffee2, 3.0)
        self.assertEqual(set(coffee.name for coffee in self.customer.coffees()), {"Latte", "Espresso"})

    def test_create_order(self):
        coffee2 = Coffee("Espresso")
        order = self.customer.create_order(coffee2, 4.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, coffee2)
        self.assertEqual(order.price, 4.0)

    def test_most_aficionado(self):
        customer2 = Customer("Bob")
        Order(customer2, self.coffee, 3.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), self.customer)  # Alice spent 5.0, Bob spent 3.0

if __name__ == "__main__":
    unittest.main()