#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in range(len(matrix)):
            for value_position in range(len(matrix[line])):
                print(matrix[line][value_position], end="")
                if value_position < len(matrix[line]) - 1:
                    print(" ", end='')
            print()
