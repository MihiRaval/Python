#!/usr/bin/env python

print("uk pizza shop")

price = float(input("Enter today's pizza price: £"))

if price <= 0:
    print("invalid price")
    exit()

pizzas = int(input("Enter number of pizzas ordered: "))

if pizzas <= 0:
    print("invalid number")

if pizzas % 2 == 0:
    # even
    full_price_pizzas = pizzas / 2
    half_price_pizzas = pizzas / 2
else:
    # odd
    full_price_pizzas = (pizzas / 2) + 1
    half_price_pizzas = (pizzas / 2) - 1

subtotal = (full_price_pizzas * price) + (half_price_pizzas * (price / 2))

# discount
if subtotal > 50:
    total = subtotal * 0.65
else:
    total = subtotal

# total price

print(f'total price:£{total:.2f}.')
