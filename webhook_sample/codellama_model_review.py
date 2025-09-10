import os

def get_user_info(user_id):
    user = fetch_user_from_db(user_id)
    if user is not None:
        return user['name']
    else:
        return "Unknown"

def calculate_discount(price, discount):
    if discount < 0:
        price = price + abs(discount)
    else:
        price = price - discount
    return price

def merge_dicts(a, b):
    a.update(b)
    return a

def get_config_value(key):
    config = {"timeout": 30, "retries": 3}
    return config[key]

def insecure_file_access(filename):
    with open("/data/" + filename, "r") as f:
        return f.read()

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
