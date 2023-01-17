#!/usr/bin/python3
"""Write a function that finds a peak"""


def find_peak(list_of_integers):
    """list_of_integers: list -> int
    return: int
    """
    size = len(list_of_integers)
    if list_of_integers == []:
        return None
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(len_of_integers)

    n = int(size / 2)
    peak = list_of_integers[n]

    if peak > list_of_integers[n - 1] and peak > list_of_integers[n + 1]:
        return peak
    elif peak < list_of_integers[n - 1]:
        return find_peak(list_of_integers[:n])
    else:
        return find_peak(list_of_integers[n + 1:])
