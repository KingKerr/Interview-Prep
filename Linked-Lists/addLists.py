"""
Let's say we have a Linked List that's representing an integer like so
7->3->9-8 is going to be 8937
Given two linked lists that are represented like this, add them up and return their sum
"""
def add_lists(l1, l2, carry = 0):

  # Set up our base case, if we don't have l1 or l2 or carry, return None
    if not l1 and not l2 and not carry:
        return None

  # Establish each node's value
    l1_value = l1.data if l1 else 0
    l2_value = l2.data if l2 else 0
    total = l1_value + l2_value + carry

  # Establish the node's next node
    l1_next = l1.next if l1 else 0
    l2_next = l2.next if l2 else 0
    carry_next = 1 if total >= 10 else 0

  # Return the sum
    return Node(total % 10, add_lists(l1_next, l2_next, carry_next))

  # Our runtime here is O(M + N) where M & N are the length of the lists.
