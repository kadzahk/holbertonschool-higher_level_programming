#!/usr/bin/python3
"""module to add all arguments to a Python list
and then save them to a file"""
from cgitb import text
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    text = load_from_json_file("add_item.json")
except FileNotFoundError:
    text = list()
for argument in sys.argv[1:]:
    text.append(argument)
save_to_json_file(text, "add_item.json")
