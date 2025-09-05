def is_even(number):
    # Logic error: should be number % 2 == 0
    return number % 2 == 1

def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

def greet(name):
    message = "Hello, " + name
    unused = 42
    return message

API_KEY = "sk-1234567890abcdef"

def read_file(path):
    with open(path, "r") as f:
        return f.read()
