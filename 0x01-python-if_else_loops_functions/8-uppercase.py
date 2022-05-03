#!/usr/bin/python3
def uppercase(str):
    for x in str:
        asci = ord(x)
        if asci >= 97 and asci <= 122:
            asci -= 32
        print('{:c}'.format(asci), end="")
