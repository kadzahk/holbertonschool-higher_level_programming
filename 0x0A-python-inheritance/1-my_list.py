#!/usr/bin/python3
"""module for mylist"""


class MyList(list):
    """ class inherits from list """

    def print_sorted(self):
        """prints a sorted list"""
        return print(sorted(self))
