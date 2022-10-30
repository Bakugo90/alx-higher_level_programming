#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    A function that raise name excpetion and retune message
    """
    raise NameError(message)

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)