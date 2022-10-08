#!/usr/bin/python3
from ast import If
import random

# assign a random signed number to the variable number each time it is executed

from symbol import if_stmt
number = random.randint(-10, 10)

# if the variable number stored is greater than 0: print is positive
if number > 0:
    print(f"{number} is positive\n")

# if the variable number stored is 0: print is zero.
if number == 0:
    print(f"{number} is zero\n")

# if the variable number stored is less than 0: print is negative.
if number < 0:
    print(f"{number} is negative\n")
