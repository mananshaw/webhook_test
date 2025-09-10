import os

def calculate_discount(price, discount):
    if discount < 0:
        price = price + abs(discount)
    else:
        price = price - discount
    return price

def unused_function():
    pass

def large_function():
    result = []
    for i in range(100):
        if i % 2 == 0:
            result.append(i * 2)
        else:
            result.append(i + 3)
    for j in range(50):
        result.append(j)
    for k in range(10):
        result.append(k * k)
    return sum(result)
