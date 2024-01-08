#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    num_cols = len(matrix)
    num_rows = len(matrix[0])

    matrix_sq = [0 for _ in range(num_cols) for _ in range(num_rows)]

    for i in range(num_rows):
        for i in range(num_cols):
            matrix[i][j] == matrix[i][j] ** 2
