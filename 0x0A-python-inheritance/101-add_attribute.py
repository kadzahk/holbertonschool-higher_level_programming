#!/usr/bin/python3
"""module from add_attribute"""


def add_attribute(obj, name, value):
    """function that adds a new attribute to an object"""

    for element in dir(obj):
        if element == '__dict__':
            setattr(obj, name, value)
            return
    raise TypeError("can't add new attribute")
