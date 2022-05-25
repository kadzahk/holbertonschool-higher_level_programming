#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """init allow square class to be used"""

    def __init__(self, size=0):
        """asign private instance attribute size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return private instance attribute size ** 2"""
        return self.__size ** 2
