"""
Write a function that takes a non-empty array of distinct integers and an integer with a target sum.

If any two numbers in the input array sum up to the target sum, the function should return them in an array.

If no 2 numbers sum up to the target sum, return an empty array.

"""

def twoNumberSum(array, targetSum):

    nums = {}

    for num in array:
        potential = targetSum - num

        if potential in nums:
            return sorted([potential, num])

        else:
            nums[num] = True

    return []
