#!/usr/bin/python3
"""module of MyInt"""


class MyInt(int):
    """class MyInt from int"""
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
