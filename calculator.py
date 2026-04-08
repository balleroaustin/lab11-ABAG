"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide")
    return b / a

def log(a, b):
    if a<=0 or b<=0 or a<=1:
        raise ValueError("invalid")
    return math.log(b,a)

def exp(a, b):
    return a**b
