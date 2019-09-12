"""

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index

Example 1:

Input -- nums = [1, 7, 3, 6, 5, 6]

Output -- 3 is the answer because of nums[3] is where numbers on left and right equal the same


Example 2:

Input -- nums = [1, 2, 3]

Output -- -1 due to no index satisfying the requirements.

Approach:

Input: [1, 7, 3, 6, 5, 6]

index: 0, num: 1, left: 0, right: 27
index: 1, num: 7, left: 1, right: 20
index: 2, num: 3, left: 8, right: 17
index: 3, num: 6, left: 11, right: 11 <-- Found!!!

"""

def pivotIndex(self, nums):

    # Set up left and right pointers
    left = 0

    right = sum(nums)

    # Begin iteration and enumerate
    # We are keeping track of the sums of all the values to the current number's left and right
    for index, num in enumerate(nums):
        #Decrement right
        right -= num

        # If they're equal, return that index
        if left == right:
            return index
        # If not, keep incrementing left
        left += num

    # Since we have nothing here, return -1
    return -1


