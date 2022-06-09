#!/usr/bin/python3
""" module of the class Student"""


class Student:
    """Class student to JSON"""
    def __init__(self, first_name, last_name, age):
        """Instantiation constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation
        of a Student instancet"""
        if attrs is None:
                return self.__dict__
        dict = {}
        for x in attrs:
            if x in self.__dict__:
                dict[x] = self.__dict__[x]
        return dict
