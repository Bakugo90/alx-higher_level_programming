#!/usr/bin/bash
#  Imports the function add
from add_0 import add

if __name__ == "__main__":

        # prints the result of the addition 1 + 2 = 3
        a = 1
        b = 2

        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
