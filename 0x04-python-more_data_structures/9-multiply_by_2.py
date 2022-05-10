#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_multi_by_2 = a_dictionary.copy()
    for i in dictionary_multi_by_2:
        dictionary_multi_by_2[i] *= 2
    return dictionary_multi_by_2
