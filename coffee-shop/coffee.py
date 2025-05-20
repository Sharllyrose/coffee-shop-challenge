
from order import Order

class Coffee:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        all_orders = self.orders()
        if not all_orders:
            return 0
        return sum(order.price for order in all_orders) / len(all_orders)