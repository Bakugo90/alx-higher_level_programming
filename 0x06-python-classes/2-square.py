#!/usr/bin/python3
"""Square
 A class that define a square

"""

class Square:
    def __init__(self, size=0):
        """__init__

        The __init__ method initialize the size value of the square

        Attributes:
            size (:obj:`int`, optional): The size of the square.

        Raises:
            TypeError: if type of size is not `int`.

            ValueError: if the value of size is less than `0`.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")

        self.__size = size
