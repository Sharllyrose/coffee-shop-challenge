
from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Oscar")
c2 = Customer("Ivy")

latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

c1.create_order(latte, 4.5)
c1.create_order(cappuccino, 6.5)
c2.create_order(cappuccino, 7.0)

print(f"{c1.name} has ordered: {[c.name for c in c1.coffees()]}")
print(f"Avg price of Cappuccino: {cappuccino.average_price()}")
print(f"Most aficionado of Cappuccino: {Customer.most_aficionado(cappuccino).name}")