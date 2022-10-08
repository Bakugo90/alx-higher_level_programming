#!/usr/bin/python3
# This program prints the ASCII alphabet, in lowercase.


for i in range(97, 123):
    if (i != 101 and i != 113):
        print('{:c}'.format(i), end="")
