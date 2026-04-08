#https://github.com/balleroaustin/lab11-ABAG.git
#Partner 1: Austin Ballero
#Partner 2: Abrahan Gil

import math

def square_root(a):
    if a < 0:
        raise ValueError("Invalid input for square root")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a,b)


def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide")
    return b / a

def logarithm(a,b):
    if a<= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for log")
    return math.log(b, a)

def exponent (a,b):
    return a**b
