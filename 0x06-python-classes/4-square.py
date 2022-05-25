#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """init allow square class to be used"""

    def __init__(self, size=0):
        """asign private instance attribute size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.size * self.size)
