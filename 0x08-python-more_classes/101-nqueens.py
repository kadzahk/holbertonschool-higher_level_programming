#!/usr/bin/python3
global queens
queens = []

def printQ():
    for i in queens:
        for row in range(8):
            if row == i:
                print(" Q",end="")
            else:
                print(" .",end="")
        print(" ")

def solve(x):
    step = len(queens) 
    for indices in range(step):
        if (x == queens[indices]):
            return False
    for i in range(step,0,-1):    
        if (x == queens[0-i]-i) or (x == queens[0-i]+i):
            return False       
    else:
        return True


def complete():
    for i in range(8):
        if solve(i) == True:
            queens += [i]
        elif solve(i) == False:
            queens = queens - [i]
        else:
            return
