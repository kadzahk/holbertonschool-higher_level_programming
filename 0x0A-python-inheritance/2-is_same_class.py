#!/usr/bin/python3
""" modele for is_same_class """


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance
    of the class otherwise will return False"""
    if obj.__class__ == a_class:
        return True
    return False
