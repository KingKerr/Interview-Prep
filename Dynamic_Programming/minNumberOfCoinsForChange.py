"""
Given an array of positive integers representing coin denominations and a single non-negative integer representing
a target amount of money, implement a function that returns the smallest number of coins needed to make change for
that target amount using the given coin denominations. If it is impossible to make change for the target amount,
return -1
"""

def minNumberOfCoinsForChange(n, denoms):

    numOfCoins = [float("inf") for amount in range(n + 1)]

    numOfCoins[0] = 0

    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])

    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


"""
Runtime = 0(Nd)

Space = 0(N)

"""
