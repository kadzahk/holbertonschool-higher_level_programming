#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divv = a / b
    except ZeroDivisionError:
        divv = None
    finally:
        print("Inside divv: {}".format(divv))
    return divv