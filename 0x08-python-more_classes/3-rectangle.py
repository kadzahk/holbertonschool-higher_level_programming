#!/usr/bin/python3
""" rectangle module for 0x08-python-more_classes """


class Rectangle:
    """ created class for our rectangule """
    def __init__(self, width=0, height=0):
        """ metod to initialize attributes  """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """setter for height"""
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Returns the Rectangle Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the Rectangle Perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Returns string representation of a Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        the_string = ""
        for x in range(self.__height):
            the_string += "#" * self.__width
            if x < self.__height - 1:
                the_string += "\n"
        return the_string
