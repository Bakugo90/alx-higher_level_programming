#!/usr/bin/python3
"""Square Class

    A Square Class

"""


class Square:
    """defining _init__function"""

    def __init__(self, size=0):
        """__init__

        The __init__ method initializes the size value of the square.

        Attributes:
            size (:obj:`int`, optional): The size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        """get the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting size to value"""
        if type(value) is not int:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value
        return self.__size

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2
