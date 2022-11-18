#!/usr/bin/python3

import random

# un program qui renvoie 5 caractère aléatoires entre a à z et 0 à 9
n = 0
v = 0

randomLetterAndNumber = []

for i in range(6):
    randomLowerLetter = chr(random.randrange(ord('a'), ord('z')))
    randomNumber = random.randrange(0, 10)

    randomLetterAndNumber.append(randomLowerLetter)
    randomLetterAndNumber.append(randomNumber)
    new = set(randomLetterAndNumber)
    print(random.choice(new), end="")

print()

for i in range(6):
    print(random.randint(0, 9), end="")
