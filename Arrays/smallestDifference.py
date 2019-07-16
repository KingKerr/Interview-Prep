"""
Write an algorithm that takes two arrays filled with integers and return a pair of numbers(this should be
one from the first array and the other from the second array) that has the smallest difference(closest to 0)

Example is:

Array1 = [-3, 2, 7, 45, 18, 55]

Array2 = [57, 30, 68, 92]

the answer here should be [55, 57]

"""

def smallestDifference(Array1, Array2):

    # First let's sort both arrays
    Array1.sort()

    Array2.sort()

    # Now we have to declare our pointers. These pointers will be used to traverse both arrays
    pointerOne = 0

    pointerTwo = 0

    # Next, we must keep track of the smallest difference. We'll set that to infinity

    smallest = float("inf")

    # Here we will keep track of the current difference and it'll also be set to infinity
    current = float("inf")

    # Let's set up an empty array to return our smallest pair

    smallest_pair = []

    # Now we have to begin our traversal of both arrays
    while pointerOne < len(Array1) and pointerTwo < len(Array2):
        # Establish variables to track values
        firstNum = Array1[pointerOne]
        secondNum = Array2[pointerTwo]

        #If the first number is smaller than the second number
        if firstNum < secondNum:
            current = secondNum - firstNum
            pointerOne += 1
        # If the second number is smaller than the first
        elif secondNum < firstNum:
            current = firstNum - secondNum
            pointerTwo += 1

        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallest_pair = [firstNum, secondNum]

    return smallest_pair
