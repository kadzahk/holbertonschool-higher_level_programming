#!/usr/bin/python3
"""module of pascal_triangle """


def pascal_triangle(n):
    """function that that returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    geo_form = [[0 for k in range(h + 1)] for h in range(n)]
    if n <= 0:
        return geo_form
    else:
        for x in range(n):
            for y in range(x + 1):
                if (y is 0 or y is x):
                    geo_form[x][y] = 1
                else:
                    geo_form[x][y] = geo_form[x - 1][y - 1] +\
                        geo_form[x - 1][y]
        return geo_form
