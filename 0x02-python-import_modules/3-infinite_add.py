#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    rel = 0
    for a in range(1, len(argv)):
        rel += int(argv[a])
    print(rel)
