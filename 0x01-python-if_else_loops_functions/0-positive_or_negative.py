#!/usr/bin/python3
import random

# assign a random signed number to the variable number each time it is executed
number = random.randint(-10, 10)

# if the variable number stored is greater than 0: print is positive
if number > 0:
    print(f"{number} is positive\n")

# if the variable number stored is 0: print is zero.
elif number == 0:
    print(f"{number} is zero\n")

# if the variable number stored is less than 0: print is negative.
elif number < 0:
    print(f"{number} is negative\n")
