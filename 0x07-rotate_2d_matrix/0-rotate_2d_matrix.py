#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates the given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.
    """
    n = len(matrix)

    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree rotation
    for i in range(n):
        matrix[i].reverse()
