#!/usr/bin/python3
"""tache 2 description d'une class vide"""


class Square:
    """ definition de la fonction init de square"""
    def __init__(self, size=0):
        """init function"""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter function for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for size"""
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        return self.__size

    def __eq__(self, s):
        """equals"""
        return self.area == s.area

    def __lt__(self, s):
        """strict sup"""
        return self.area < s.area

    def __le__(self, s):
        """sup or equals"""
        return self.area <= s.area

    def __ne__(self, s):
        """negative"""
        return self.area != s.area

    def __gt__(self, s):
        """strict inf"""
        return self.area > s.area

    def __ge__(self, s):
        """inf or equals"""
        return self.area >= s.area
