"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

"""

def uniqueOccurrences(self, arr):
    freq_count = {}

    count_map = {}

    # Iterate thru the array
    for num in arr:
        # If we see the integer already in the hash table, update the count
        if num in freq_count:
            freq_count[num] += 1
        # If not, add it's first occurrence
        else:
            freq_count[num] = 1

    # Now we iterate thru the frequency count hash table
    for count in freq_count:
        # if we see the iterator in the second hash table, that means
        # we have multiple occurrences, therefore this is False
        if freq_count[count] in count_map:
            return False
        # If not, we'll update the count_map hash table to reflect that iterator
        count_map[freq_count[count]] = 0
    return True
