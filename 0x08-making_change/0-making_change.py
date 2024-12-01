#!/usr/bin/python3
""" Making Change problem solution module """


def makeChange(coins, total):
    """ Returns the minimum number of coins to make a given total using a list
    of denominations """
    if total < 1:
        return 0

    sorted_coins = sorted(coins, reverse=True)

    count = 0
    working_total = total

    for coin in sorted_coins:
        if working_total >= coin:
            count += working_total // coin
            working_total %= coin

        if working_total == 0:
            return count

    return -1
