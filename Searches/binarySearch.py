"""
Implement a Binary Search Algorithm

"""

def binarySearch(array, target):
    # Establish low
    low = 0
    # Establish high
    high = len(array) - 1

    # Begin traversal
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1
