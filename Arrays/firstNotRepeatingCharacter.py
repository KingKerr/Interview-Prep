"""
Given a string that consists of small English letters,
find and return the first instance of a non-repeating character in it.

If there is none, return '_'.

"""

def firstNotRepeatingCharacter(s):
  # First step is to convert our string to a list
  my_list = list(s)

  # This is our Dictionary/Hash Map.. We'll use this to track duplicate characters
  dupe_char = {}

  # Here is an empty array that we'll append any character that's seen for the first time
  new_list = []

  # Base case, if list is less than 2 characters, return the '_'
  if len(my_list) < 1:
    return '_'

  # Begin our iteration over list, we'll check if the character is a dupe or not
  # If it is, update the count, if it isn't, add to our new_list
  for i in my_list:
    if i in dupe_char:
      dupe_char[i] += 1

    else:
      dupe_char[i] = 1
      new_list.append(i)

  # Make sure to iterate over the new list and check which characters only appear once, whenever we have one
  # just return it.
  for i in new_list:
    if dupe_char[i] == 1:
      return i

  return '_'
