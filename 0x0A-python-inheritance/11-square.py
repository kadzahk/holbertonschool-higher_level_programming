#!/usr/bin/python3
"""module based in BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square from Rectangle"""

    def __init__(self, size):
        """initializes variables and methods"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


def __str__(self):
    """prints a string representation of the Square"""
    return "[Square] {}/{}".format(self.__size, self.__size)
