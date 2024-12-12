#!/usr/bin/python3
""" isWinner function module
"""


def isWinner(x, nums):
    """ returns the player that won the most rounds in the prime game
    """
    Ben = 0
    Maria = 0
    for round in range(x):
        prime = [True for i in range(nums[round] + 1)]
        p = 2

        while (p * p <= nums[round]):
            if prime[p] is True:
                for i in range(p * p, nums[round] + 1, p):
                    prime[i] = False
            p += 1
        primeOnly = [pn for pn in range(2, nums[round] + 1) if prime[pn]]

        if len(primeOnly) > 0:
            if len(primeOnly) % 2 == 0:
                Ben += 1
            else:
                Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None
    if Ben > Maria:
        return 'Ben'
    return 'Maria'
