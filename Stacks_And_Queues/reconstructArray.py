"""
Reconstruct an array using +/- signs

You have a jumbled sequence [0, 1, ..., N] and you need to reconstruct an array that is consistent with it using
only plus(+) and minus(-) signs. An example is:
[None, +, +, -, +] and you can return [1, 2, 3, 0, 4]

"""

def reconstructArray(array):
    answer = []
    n = len(array)
    stack = []

    for i in range(n):
        if array[i + 1] == '-':
            stack.append(i)
        else:
            answer.append(i)
            while stack:
                answer.append(stack.pop())
    stack.append(n)
    while stack:
        answer.append(stack.pop())
    return answer


"""

Runtime is 0(N) and space.
"""
