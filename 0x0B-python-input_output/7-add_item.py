#!/usr/bin/python3
"""module of add_items"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """function that adds all arguments to a Python list
    and then saves them to a file"""
    try:
        python_list = load_from_json_file('add_item.json')
    except:
        python_list = []

    for x in range(1, len(sys.argv)):
        python_list.append(sys.argv[x])

    save_to_json_file(python_list, 'add_item.json')

if __name__ == '__main__':
    add_items()
