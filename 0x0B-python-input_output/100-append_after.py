#!/usr/bin/python3
"""module of append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file
    after each line containing a specific string"""
    with open(filename, 'r+') as r:
        mul = r.readlines()
        x = 0
        for one in mul:
            if one.find(search_string) is not -1:
                mul.insert(x + 1, new_string)
            x += 1
        r.seek(0)
        r.write("".join(mul))
