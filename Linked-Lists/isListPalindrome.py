"""
Given a singly, linked list of integers.. Determine whether it's a palindrome or not.

"""

def isListPalindrome(l):

    head = l

    if not head or not head.next:
        return True


  # 1.) Our first step is to get to the midpoint of the list
  # The midpoint is slow
    slow = fast = cur = head

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next


  # 2.) Next, push the second half into the stack
    stack = [slow.value]

    while slow.next:
        slow = slow.next
        stack.append(slow.value)

  # 3.) Lastly, we'll compare the values to see if they're a Palindrome or not

    while stack:
        if stack.pop() != cur.value:
            return False

    cur = cur.next

    return True

# The runtime for this Algorithm is 0(N) and the space complexity is 0(1)
