#!/usr/bin/python3
def no_c(my_string):
    n_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            n_string += char
    return n_string
