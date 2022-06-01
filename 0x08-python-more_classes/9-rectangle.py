#!/usr/bin/python3
""" rectangle module for 0x08-python-more_classes """


class Rectangle:
    """ created class for our rectangule """
    """ class attribute"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ metod to initialize attributes  """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns string representation of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        new_string = ""
        for x in range(self.__height):
            new_string += str(self.print_symbol) * self.__width
            if x < self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """Returns a String with a representation of the state of the object"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """printthe message at deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Function that returns the biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
