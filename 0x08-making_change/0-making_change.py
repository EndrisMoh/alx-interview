#!/usr/bin/python3
"""
 Making change
"""
 
def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount total.

    Args:
        coins: A list of the values of the coins in your possession.
        total: The amount of money you need to make change for.

    Returns:
        The fewest number of coins needed to meet total.
        If total is 0 or less, returns 0.
        If total cannot be met by any number of coins you have, returns -1.
    """
    if total <= 0:
        return 0

    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
