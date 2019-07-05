"""
Given an array of integers that aren't in order, determine the bounds of the smallest window that
has to be sorted in order for the entire array to be sorted.

An example is: [3, 7, 5, 6, 9] and that should return --> (1, 3)

"""

"""
Solution: We will traverse the array, from left to right and track the maximum & minimum
we've seen up to that point. We'll set the maximum and use it as our right bound and set the minimum
to be our left bound. Once we're done, we'll just return both of them.
"""
def smallest_window(array):

  # Here we are establishing the left & right bounds
    left, right = None, None

  # Next, we'll set the variable for the length of the array. This is important since we'll be traversing
    n = len(array)

  # Here we're going to establish our max and min variables
    max_seen, min_seen = -float("inf"), float("inf")

  # Now we're traversing the array for the right bound
    for i in range(n):
    # Update max to reflect the current iterator
        max_seen = max(max_seen, array[i])

    # If that last value is less than max, update that to be our right bound
        if array[i] < max_seen:
            right = i

  # Here we're traversing the array again, this time backwards so we can get the left bound
    for i in range(n - 1, -1, -1):
    # Update min to reflect the current iterator
        min_seen = min(min_seen, array[i])
    # If that last element is greater than min, set the left bound
        if array[i] > min_seen:
            left = i

  # When we're done, return both bounds
    return left, right

  # Our runtime here is 0(N) due to having to traverse the entire array twice and the space is 0(1).
