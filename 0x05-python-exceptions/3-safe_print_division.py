#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divv = a / b
        print("Inside result: {:.1f}".format(divv))
    except ZeroDivisionError:
        divv = None
        print("Inside result: {}".format(divv))
    finally:
        return divv
