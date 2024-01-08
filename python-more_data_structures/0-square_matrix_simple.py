#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix:
        return[]

    matrix_sq = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    for i in range(matrix):
        for j in range(matrix[0]):
            matrix[i][j] = matrix[i][j] ** 2

    return matrix_sq
