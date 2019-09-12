"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

input -- J = "aA", S = "aAAbbbb"

output -- 3

Example 2:

input -- J = 'z', S = "ZZ"

output -- 0

"""


def numJewelsInStones(self, J, S):
    count = 0

    for i in S:
        if i in J:
            count += 1
        else:
            continue
    return count
