#!/usr/bin/python3
"""module of BaseGeometry"""


class BaseGeometry:
    """ class BaseGeometry"""

    def area(self):
        """raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
