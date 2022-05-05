#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if a == 1:
        print(f"{a - 1} arguments.")
    elif a == 2:
        print(f"{a - 1} argument:")
    else:
        print(f"{a - 1} arguments:")
    for x in range(1, a):
        print(f"{x}: {argv[x]}")
