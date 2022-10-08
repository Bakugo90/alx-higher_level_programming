#!/usr/bin/python3
from contextlib import nullcontext
import random

# Assign a random signed number to the variable number each time it is executed
number = random.randint(-10000, 10000)

# Get the string representation
num_str = repr(number)

# Get the Last string of the variable number
last_str = num_str[-1]

# Convert Last string into an integer
lastInt = int(last_str)

# if lastDigit  is greater than 5
if lastInt > 5:
    print(f"Last digit of {number} is {lastInt} and is greater than 5")

# if lastDigit  is less than 6
elif lastInt < 5:
    print(f"Last digit of {number} is {lastInt} and is less than 6 and not 0")

# if lastDigit  is 0: lastDigit of number is lastDigit.
elif lastInt == 0:
    print(f"Last digit of {number} is {lastInt} and is 0")
