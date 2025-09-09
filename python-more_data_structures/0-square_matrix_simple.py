#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[1]] * len(matrix)
    row_idx = 0
    for row in matrix:
        new_matrix[row_idx] = [x*x for x in row]
        row_idx += 1
    return new_matrix
