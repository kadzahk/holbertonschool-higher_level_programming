#!/usr/bin/python3
""" module of read_file"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, 'r') as f:
        return len(f.readlines())
