"""
Given an array that contains number in the range from 1 to length of array, find the first duplicate number

for which the second occurrence has the minimal index.

Example is as follows --

a = [2, 1, 3, 5, 3, 2]

The answer here should be 3. Even though we have 2 duplicates -- 2 & 3, the 2nd occurrence of 3 has a smaller index
than the 2nd occurrence of 2.

"""

def firstDuplicate(a):
  # Here we are setting up our Hashset
    S = set()

  # If our list is less than 2 elements, return the default
    if len(a) < 2:
        return -1

  # Begin our iteration, check to see if element is a duplicate or not..

  # if it is not, add it to the set, if it is just return it

  # Since we're returning the element with the smallest index, this will work
    for i in a:
        if i not in S:
          S.add(i)

        else:
          return i

  # Return default
    return -1
