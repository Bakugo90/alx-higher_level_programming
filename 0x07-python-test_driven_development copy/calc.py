#!usr/bin/python3

"""calc.py
    This module performs some basics operation like addition, soustraction etc...
"""

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError('Can\'t divide by 0')
    return a / b
