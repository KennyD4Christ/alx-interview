#!/usr/bin/python3
"""
Module for determining the fewest number of coins needed to meet a given
amount, given a pile of coins of different values
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): List of coin values available.
    total (int): The total amount to achieve with the given coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Update dp array for each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check the result for the given total
    return dp[total] if dp[total] != float('inf') else -1
