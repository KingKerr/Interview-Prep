"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
Input is [3, 1, 2, 4]

Output is [ 2, 4, 3, 1] other accepted outputs would have been:

[4, 2, 3, 1], [2, 4, 1, 3] and [4, 2, 1, 3]



Solution:
Use 2-pointers, start and end. Whenever start is odd, decrease end until end is even or end > start, then switch them.

"""

def sortArrayByParity(self, A):

    # Setup 2 pointers
    start = 0
    end = len(A) - 1
    # Begin traversal with while loop
    while start < end:
        if A[start] % 2:
            while end > start and A[end] % 2:
                end -= 1
            # Swap
            A[end], A[start] = A[start], A[end]
        start += 1
    return A



