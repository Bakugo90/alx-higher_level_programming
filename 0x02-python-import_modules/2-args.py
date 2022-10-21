#!/usr/bin/python3
import sys

if __name__ == "__main__":

    """
     A program that prints the number of and the list of its arguments.

    """

    argm = sys.argv
    if len(argm) - 1 == 0:
        print(len(argm) - 1, "arguments.")
    elif len(argm) - 1 == 1:
        print(len(argm) - 1, "arguments:")
        for i in range(1, len(argm)):
            print("{:d}: {:s}".format(i, argm[i]))
    elif len(argm) - 1 > 1:
        print(len(argm) - 1, "arguments:")
        for i in range(1, len(argm)):
            print("{:d}: {:s}".format(i, argm[i]))
