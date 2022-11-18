#!/usr/bin/python3
"""tache 2 description d'une class vide"""


class Square:
    """ definition de la fonction init de square"""

    def __init__(self, size=0, position=(0, 0)):
        """init function"""

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not (isinstance(position, tuple)) or len(position) != 2 \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    def my_print(self):
        """printf function"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")

            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """getters functiion for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter functions for position"""
        if not (isinstance(value, tuple)) or len(value) != 2 or value[0] < 0 \
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        return self.__position

    def __str__(self):
        """string printer"""
        string = ""
        if self.__size == 0:
            return ""

        string +=\
            "\n" * self.__position[1] + \
            (" " * self.__position[0] + "#" * self.__size + "\n") * self.__size

        return string[:-1]
