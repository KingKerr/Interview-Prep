"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

def plusOne(self, digits):

    num = 0

    # Begin iteration
    for i in range(len(digits)):
        # Increment num by the current index and multiply it by 10 to the length of the list minus the 1 and the iterator
        # This will be an exponent
        num += digits[i] * pow(10, (len(digits)-1-i))

    # Return the integer for the iterator as a string
    return [int(i) for i in str(num + 1)]
