#!/usr/bin/python3
""" This is the LockedClass module """


class LockedClass:
    """
    Special class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name """

    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """initializes attribute first_name"""
        self.first_name = first_name
