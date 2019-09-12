"""
Write a function that takes a string as input and reverses only the vowels of a string

Example 1: input: 'hello' output: 'holle'

Example 2: input: 'leetcode' output: 'leotcede'

"""

def reverseVowels(self, s):
    # Store vowels in string
    vowels = 'aeiouAEIOU'

    # Convert input string to list
    s = list(s)

    # We'll use two pointers to iterate thru list
    # First index
    start = 0

    # Last index
    end = len(s) - 1

    # Begin iterating with while loop
    while start < end:
        # If both indexes are vowels
        if s[start] in vowels and s[end] in vowels:
            # Swap and then continue iterating
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        # If start isn't in vowels, keep iterating
        elif s[start] not in vowels:
            start += 1

        # If end isn't in vowels, keep iterating
        elif s[end] not in vowels:
            end -= 1
    # Return input string as a string again
    return ''.join(s)
