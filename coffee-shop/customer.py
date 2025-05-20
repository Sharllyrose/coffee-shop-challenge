
from order import Order

class Customer:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @staticmethod
    def most_aficionado(coffee):
        most = None
        most_orders = 0
        for customer in {order.customer for order in coffee.orders()}:
            count = sum(1 for order in customer.orders() if order.coffee == coffee)
            if count > most_orders:
                most = customer
                most_orders = count
        return most
    @classmethod
    def most_aficionado(cls, coffee):
        customer_spend = {}
        for order in Order.all:
            if order.coffee == coffee:
                customer_spend[order.customer] = customer_spend.get(order.customer, 0) + order.price
        if not customer_spend:
            return None
        return max(customer_spend, key=customer_spend.get)