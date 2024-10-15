#!/usr/bin/python3
"""This module contains a function that calculates the fewest number of
operations needed to result in exactly n H characters in the file."""


def minOperations(n):
    """This function calculates the fewest number of operations needed to
    result in exactly n H characters in the file."""
    if n <= 1:
        return 0
    operations = 0
    number = n
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            operations += divisor
            number /= divisor
        else:
            divisor += 1

    return operations
