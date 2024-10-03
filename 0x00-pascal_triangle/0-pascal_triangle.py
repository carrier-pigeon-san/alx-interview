"""
This module contains the pascal_triangle(n) function
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    main_list = []
    if (n):
        for i in range(n):
            small_list = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    small_list.append(1)
                else:
                    j = main_list[i - 1][j] + main_list[i - 1][j - 1]
                    small_list.append(j)
            main_list.append(small_list)
    return main_list
