#!/usr/bin/puthon3
import sys

if __name__ == "__main__":

    """
     A program that prints the result of the addition of all arguments.

    """
    sum = 0
    argm = sys.argv
    for i in range(1, len(argm)):
        sum += int(argm[i])

    print(sum)