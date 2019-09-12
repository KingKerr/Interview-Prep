"""
Given an array of integers and a number k, where 1 <= k <= array length, compute the maximum values of each
subarray of length k

An example is:
[10, 5, 2, 7, 8, 7] and k = 3

This will return [10, 7, 8, 8]

"""

from collections import deque

def max_of_subarrays(lst, k):
    q = deque()

    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)


    for i in range(k, len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])

"""
Runtime is O(N) and space is O(K)

"""
