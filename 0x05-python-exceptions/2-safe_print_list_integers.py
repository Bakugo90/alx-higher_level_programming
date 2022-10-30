#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    A function that prints the first x elements of a list and only integers.
    """
    idx = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and idx != x:
                print("{:d}".format(my_list[i]), end="")
                idx += 1

        except TypeError:
            continue
    print()

    return idx
