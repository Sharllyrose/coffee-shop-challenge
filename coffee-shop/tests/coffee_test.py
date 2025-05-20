
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A")
    with pytest.raises(ValueError):
        Coffee(123)

    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

def test_coffee_orders_and_customers():
    coffee = Coffee("Americano")
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    o1 = c1.create_order(coffee, 3.5)
    o2 = c2.create_order(coffee, 4.5)

    assert o1 in coffee.orders()
    assert o2 in coffee.orders()
    assert c1 in coffee.customers()
    assert c2 in coffee.customers()

def test_coffee_aggregates():
    coffee = Coffee("Flat White")
    c1 = Customer("Ali")
    c2 = Customer("Bea")
    c1.create_order(coffee, 5.0)
    c2.create_order(coffee, 7.0)

    assert coffee.num_orders() == 2
    assert round(coffee.average_price(), 2) == 6.00