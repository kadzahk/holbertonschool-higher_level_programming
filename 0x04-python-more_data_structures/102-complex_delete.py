#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keyz = list(a_dictionary.keys())
    valuez = list(a_dictionary.values())
    for i, key in enumerate(keyz):
        if value is valuez[i]:
            del a_dictionary[key]
    return a_dictionary
