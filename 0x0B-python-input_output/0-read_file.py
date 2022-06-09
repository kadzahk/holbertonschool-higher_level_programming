#!/usr/bin/python3
""" module of read_file"""


def read_file(filename=""):
    """reads a text file and prints it"""
    with open(filename, 'r') as r:
        file_text = r.read()
        print(file_text, end='')
