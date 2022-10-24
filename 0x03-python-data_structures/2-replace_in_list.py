#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    A function that replaces an element of a list at a specific position.

    my_list : A list that we'll be used for the operation
    idx :  Element index
    element: Element which we'lll be replaced
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
