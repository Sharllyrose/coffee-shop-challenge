
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # Too short
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Too long
    with pytest.raises(ValueError):
        Customer(123)  # Not a string

    c = Customer("Oscar")
    assert c.name == "Oscar"

def test_customer_orders_and_coffees():
    c = Customer("Jane")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    o1 = c.create_order(coffee1, 4.5)
    o2 = c.create_order(coffee2, 5.5)

    assert o1 in c.orders()
    assert o2 in c.orders()
    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()