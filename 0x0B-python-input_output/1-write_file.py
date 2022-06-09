#!/usr/bin/python3
""" module of number_of_lines"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, 'r') as r:
        return len(r.readlines())
