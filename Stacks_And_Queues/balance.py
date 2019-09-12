"""
Given a string of round, curly, and square opening and closing brackets, return whether the brackets are balanced(well-formed)

"""

def balance(s):
    stack = []

    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False

            if (char == ")" and stack[-1] != "(") or \
               (char == "]" and stack[-1] != "[") or \
               (char == "}" and stack[-1] != "{") :
                return False
            stack.pop()

    return len(stack) == 0


"""
Runtime is 0(N) and Space is 0(N)

"""
