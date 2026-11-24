"""
    Decorators: its a flixable way to extend the function or methods behaviour. 
    A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality. 
"""

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))