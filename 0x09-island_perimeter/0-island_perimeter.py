#!/usr/bin/python3
"""This module contains the island_perimeter function that determines the
the perimeter of an island as described by a 2D array """


def island_perimeter(grid):
    """ returns the perimeter of the island described in the grid """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0:
                    perimeter += 1
                elif grid[i - 1][j] == 0:
                    perimeter += 1

                if j == 0:
                    perimeter += 1
                elif grid[i][j - 1] == 0:
                    perimeter += 1

                if i == len(grid) - 1:
                    perimeter += 1
                elif grid[i + 1][j] == 0:
                    perimeter += 1

                if j == len(grid[i]) - 1:
                    perimeter += 1
                elif grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
