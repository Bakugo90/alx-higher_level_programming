#!/usr/bin/python3
"""Square Class

 A square class

"""


class Square:
    """Defining the init method of the square"""
    def __init__(self, size):
        """__init__

        The __init__ method initializes the size value
        of the square.

        Args:
            size: size of square.

        Attributes:
            size (int): protected attrineutes instances.

        """
        self.__size = size
