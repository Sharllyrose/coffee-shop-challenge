
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)