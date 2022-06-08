#!/usr/bin/python3
"""module of BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializes variables and methods for the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
