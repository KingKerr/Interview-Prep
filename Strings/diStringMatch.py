"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:
Input: 'IDID'
Output: [0, 4, 1, 3, 2]

Example 2:
Input: 'III'
Output: [0, 1, 2, 3]

Example 3:
Input: 'DDI'
Output: [3, 2, 0, 1]


Steps to solution:

        1.) Store results in an empty array. Set up variables for maxNum of permutations(len(S)) and minNum of permutations(which is 0).

        2.) Iterate thru the String, checking each character to see if 'I' or 'D'. If 'I', we append minNum to the results array, and then increment.
            If 'D', we will append maxNum to results array, then decrement maxNum.
        3.) Once we iterated thru the entire string, append the last character. Return results array.


"""

def diStringMatch(self, S):
    # Store results here
    results = []

    maxNum = len(S)

    minNum = 0

    # Begin iterating thru string
    for i in S:
        # Check to see if character is an 'I'
        if i == 'I':
            # if so, append the minimum
            results.append(minNum)
            # Update the count so we're accurate
            minNum += 1
        else:
            # If it's 'D', add the max
            results.append(maxNum)
            # Update the count here
            maxNum -= 1
    # Add the last character in String
    results.append(maxNum)
    # Return results
    return results

