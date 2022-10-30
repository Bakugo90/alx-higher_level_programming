#!/usr/bin/python3

def safe_print_division(a, b):
    """
     A function that divides 2 integers and prints the result.
    """
    try:
        ans = a / b
        # print("Inside result: {}".format(ans))
        # return ans
    except ZeroDivisionError:
        ans = None
    finally:
        print("Inside result: {}".format(ans))
        return ans
