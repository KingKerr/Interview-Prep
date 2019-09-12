"""
Roman numerals are represented by 7 different symbols: I, V, X, L, C, D & M. Given a roman numeral, convert
it to an integer. Input is guaranteed to be within the range from 1 to 3999. There are 6 instances where substraction
can be used:
'I' can be placed before 'V' to make 4.
'I' can be placed before 'X' to make 9.

'X' can be placed before 'L' to make 40.
'X' can be placed before 'C' to make 90.

'C' can be placed before 'D' to make 400.
'C' can be placed before 'M' to make 900.

Example input: 'III' will return 3


Example 2: 'IX' will return 9

Example 3: 'LVIII' will return 58

"""


def romanToInt(s):
    # Here we'll store our symbols in a Hash Table
    # that way we can map to our value easily

    symbols_to_map {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # This is what we'll use to return our answer
    answer = 0

    # Begin iterating over the string
    for i in range(len(s)):

        # Here we are checking to see if we're NOT at the 2nd to last value near end of the string
        # and if the iterator's value is less than the next value:
        # an example is 'IV' where 'I' is less than 'V'
        if i < len(s) - 1 and symbols_to_map[s[i + 1]] > symbols_to_map[s[i]]:
            # If that's the case, we subtract that value from our answer
            answer = -= symbols_to_map[s[i]]

        # If not, just add. An example is 'XI'. Since 'X' is greater
        # than 'I', you'll have to add those two values.
        else:
            answer += symbols_to_map[s[i]]

    # Return your answer.
    return answer
