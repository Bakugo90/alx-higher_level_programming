#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
     A function that prints a matrix of integers.
    """
    if matrix:
        for row in matrix:
            i = 1
            length = len(row)

            for elems in row:
                if i == length:
                    print("{:d}".format(elems), end="")
                else:
                    print("{:d}".format(elems), end=" ")
                    i += 1
            print()
