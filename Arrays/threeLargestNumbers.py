"""
Objective is to find 3 largest numbers in a non-sorted array and return those in a sorted array

Example:

input: [141, 2, 17, -7, -17, -27, 18, 541, 8, 7, 7]

output: [18, 141, 541]

"""


def threeLargestNumbers(array):
    # Establish fixed array with 3 total indexes
    threeLargest = [None] * 3

    # Iterate thru our input array
    for num in array:
        # Call a helper function to update the largest value
        updateLargest(threeLargest, num)
    # Return the fixed array
    return threeLargest


def updateLargest(threeLargest, num):
    # Here is our helper function where we update the largest value based on index
    if threeLargest[2] is None or num > threeLargest[2]:
        # We've created another helper function where we can shift and update the values accordingly
        shiftandUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftandUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftandUpdate(threeLargest, num, 0)

def shiftandUpdate(array, num, idx):
    # This is another helper function where we shift and update the values in our array accordingly
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


"""

Runtime: O(N) -- Linear due to iterating thru entire array(N is length of array)

Space: O(1) -- constant space due to not storing anything more than the 3 indexes in our final array.
"""
