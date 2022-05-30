#!/usr/bin/python3
""" Fucntion that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """

    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    row_error = "Each row of the matrix must have the same size"
    num_error = "div must be a number"
    zerp_error = "division by zero"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(list_error)
    for element in matrix:
        if not isinstance(element, list):
            raise TypeError(list_error)

        if len(matrix[0]) is not len(element):
            raise TypeError(row_error)
        for j in element:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(list_error)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(num_error)
    if div == 0:
        raise ZeroDivisionError(zerp_error)

    return[[round(j / div, 2) for j in i] for i in matrix]