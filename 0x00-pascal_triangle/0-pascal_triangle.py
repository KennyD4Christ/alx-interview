#!/usr/bin/python3
"""
Module for generating Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Parameters:
    n (int): Number of rows in the triangle

    Returns:
    list: List of lists representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        prev_row = triangle[-1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
