#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_multi_by_2 = a_dictionary.copy()
    return [list(map(lambda x: x * 2, b)) for b in dictionary_multi_by_2]
