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

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))