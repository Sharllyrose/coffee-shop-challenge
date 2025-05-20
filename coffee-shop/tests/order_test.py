
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    c = Customer("Tim")
    coffee = Coffee("Cappuccino")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)  # Below range
    with pytest.raises(ValueError):
        Order(c, coffee, 11.0)  # Above range
    with pytest.raises(TypeError):
        Order("NotCustomer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(c, "NotCoffee", 5.0)

    o = Order(c, coffee, 4.0)
    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 4.0

def test_order_is_registered():
    Order.all.clear()
    c = Customer("Timmy")
    coffee = Coffee("Macchiato")
    o = Order(c, coffee, 6.0)
    assert o in Order.all