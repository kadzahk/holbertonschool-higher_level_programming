#!/usr/bin/python3
"""Define Rectangle Class"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Module Representation of Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size, retrieves size value"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size, validates the size value assignement"""
        self.width = value
        self.height = value

    def __str__(self):
        """string represation of square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """update the data of the square with a kwargs"""
        key_list = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0 and len(args) <= 5:
            for i, arg in enumerate(args):
                setattr(self, key_list[i], arg)
        if kwargs is not None and len(kwargs) > 0 and len(kwargs) <= 5:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """retrun dictonary a dictionary of id, size, x and y"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
