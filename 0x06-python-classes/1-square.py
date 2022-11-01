#!/usr/bin/python3
"""Square Class

 A square class

"""


class Square:

    def __init__(self, size):

        """__init__

        The __init__ method initializes the size value
        of the square.

        Args:
            self: is used to point to object itself.
            size: size of square

        Attributes:
            size (int): The size of the square.

        """
        self.__size = size
