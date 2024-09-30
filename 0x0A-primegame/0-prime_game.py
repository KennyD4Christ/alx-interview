#!/usr/bin/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    :param x: number of rounds
    :param nums: array of n for each round
    :return: name of the player that won the most rounds
             or None if the winner cannot be determined
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes to find primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False

    # Count primes up to each number in nums
    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(2, max_num + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 > x:
        return "Maria"
    elif maria_wins * 2 < x:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
