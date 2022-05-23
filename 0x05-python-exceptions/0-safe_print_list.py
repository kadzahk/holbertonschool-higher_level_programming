#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cc = 0 
        while cc < x:
            print(my_list[cc], end="")
            cc +=1
        print()
    except IndexError:
        print()
    finally:
        return cc
