#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 0:
        y = x
    else:
        y = x - 32
    print("{:c}".format(y), end="")
