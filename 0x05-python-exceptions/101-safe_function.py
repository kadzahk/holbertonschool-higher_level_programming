#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        rel = fct(*args)
        return rel
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        return None
