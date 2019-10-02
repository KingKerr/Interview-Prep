"""
Given an array of numbers, find the maximum sum of any contiguous subarray
of the array. An example is:

Given this array [34, -50, 42, 14, -5, 86], the maximum sum would be 137 since we'd take elements
42, 14, -5 and 86.

A follow-up would be: What if the elements can wrap around? An example would be [8, -1, 3, 4]

this should return 15 since we're using 8 which is the number that wrapped around.

"""


def maximum_circular_subarray(arr):
    max_subarray_sum_wraparround = sum(arr) - min_subarray_sum(arr)

    return max(max_subarray_sum(arr), max_subarray_sum_wraparround)



"""
We're going to go with Kadane's Algorithm here.

"""

def max_subarray_sum(arr):
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def min_subarray_sum(arr):
    min_ending_here = 0
    min_so_far = 0

    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far
