"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

"""

def dominantIndex(self, nums):

    largest = nums[0]

    second_largest = -float('inf')

    largest_index = 0

    for idx in range(1, len(nums)):
        if nums[idx] > largest:
            second_largest = largest
            largest = nums[idx]
            largest_index = idx
        elif nums[idx] > second_largest:
            second_largest = nums[idx]
    return largest_index if largest >= second_largest * 2 else -1
