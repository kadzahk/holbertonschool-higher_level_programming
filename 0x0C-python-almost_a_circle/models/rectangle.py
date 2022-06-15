#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method __init__ Initialization a Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width, retrieves width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width, validates the value assignment for width"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    @property
    def height(self):
        """getter for height, retrieves height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height, validates the value assignment for height"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    @property
    def x(self):
        """getter for x, retrieves x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x, validates the value assignment for x"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    @property
    def y(self):
        """getter for y, retrieves y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y, validates the value assignment for y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def update(self, *args, **kwargs):
        """method update """
        a_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > 0 and len(args) <= 5:
            for i, arg in enumerate(args):
                setattr(self, a_list[i], arg)
        if kwargs is not None and len(kwargs) > 0 and len(kwargs) <= 5:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def __str__(self):
        """method that """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def area(self):
        """public_method area of rectangle """
        return self.width * self.height

    def display(self):
        """public method display self prints in stdout """
        pattern = ""
        if self.width is 0 or self.height is 0:
            print(pattern)
        else:
            for k in range(self.y):
                pattern += '\n'
            for j in range(self.height):
                for h in range(self.x):
                    pattern += ' '
                for i in range(self.width):
                    pattern += '#'
                if j is not (self.height - 1):
                    pattern += '\n'
            print(pattern)

    def to_dictionary(self):
        """function that returns the dictionary representation
        of a Rectangle
        object/instance"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
