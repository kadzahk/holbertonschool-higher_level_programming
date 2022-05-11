#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or not isinstance(roman_string, str):
        return 0
    rel = 0
    romanz = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    chars_of_the_string = len(roman_string)
    for i in range(chars_of_the_string):
        if i != chars_of_the_string - 1 and (romanz[roman_string[i + 1]] > romanz[roman_string[i]]):
            rel -= romanz[roman_string[i]]
        else:
            rel += romanz[roman_string[i]]
    return rel
