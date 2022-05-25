#!/usr/bin/python3
""" class square """


class Square:
    """start of a class with setting size """

    def __init__(self, size=0):
        """setting size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return size **2"""
        return self.__size ** 2

    def __lt__(self, other):
        """verify situation"""
        return self.area() < other.area()

    def __le__(self, other):
        """verify situation"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """verify situation"""
        return self.area() == other.area()

    def __ne__(self, other):
        """verify situation"""
        return self.area() != other.area()

    def __gt__(self, other):
        """verify situation"""
        return self.area() > other.area()

    def __ge__(self, other):
        """verify situation"""
        return self.area() >= other.area()
