#!/usr/bin/python3
"""Square
A class that define a square.

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

        self.size = size

    @property
    def size(self):
        """getter the size value"""
        return self.__self
    @size.setter
    def size(self, value):
        """sttter the size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def area(self):
        """Area return the area of the square"""
        return self.__size ** 2


