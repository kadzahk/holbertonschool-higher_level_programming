#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rel = 0
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    chars = len(roman_string)
    for i in range(chars):
        if i != chars - 1 and (rd[roman_string[i + 1]] > rd[roman_string[i]]):
            rel -= rd[roman_string[i]]
        else:
            rel += rd[roman_string[i]]
    return rel
