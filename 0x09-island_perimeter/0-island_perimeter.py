#!/usr/bin/python3
"""
This module contains the function island_perimeter.
The function calculates the perimeter of the island described in the grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A list of lists where 0 represents water
        and 1 represents land. Cells are square with a
        side length of 1 and are connected horizontally
        and vertically.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start with 4 sides of a land cell
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
