#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list.
    """
    idx = 0

    try:
        for i in my_list:
            if idx < x:
                print("{}".format(my_list[idx]), end="")
                idx += 1

        print()

    except TypeError:
        pass
    finally:
        return idx
