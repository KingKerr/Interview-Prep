"""
Single Cycle Check.. Given an array of integers that represents a jump of it's value in the array. If your integer is 2, then you
have to jump 2 indices forward. If the integer is -5, then you have to jump 5 indices backwards. If your jump exceeds the bounds of the array,
it wraps over.

Examples:
[2, 3, 1, -4, -4, 2] will return True

[1, -1, 1, -1] will return False.

"""


def hasSingleCycle(array):
    numOfElementsVisited = 0
    currentIdx = 0
    while numOfElementsVisited < len(array):
        if numOfElementsVisited > 0 and currentIdx == 0:
            return False
        numOfElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == 0

def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    # We're dividing by length of array to account for large integers or negative ones
    nextIdx = (jump + currentIdx) % len(array)

    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
