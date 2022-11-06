#!/usr/bin/python3
"""Sqaure
A class that defines a sqaure.

"""


class Square:
    """Defining the init method"""
    def __init__(self, size=0):
        """__init__

        Initialize the size value to square.

        Attributes:
            size (int): the size of the square.

        Raises:
            TypeError: if the type of size is not 'int'.

            ValueError: if the value ogf size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method return the are of square"""
        return self.__size**2
