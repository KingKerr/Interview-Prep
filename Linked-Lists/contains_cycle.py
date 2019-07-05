# You have a Singly-Linked List and want to check if it contains a cycle.

# A Cycle is when the Node's 'next' pointer points back to a previos node in the linked list.


def contains_cycle(first_node):
  # Establish 2 pointers at the head
    slow_runner = first_node
    fast_runner = first_node

  # Begin traversing the List while you can
    while fast_runner is not None and fast_runner.next is not None:
    # Establish one pointer as slow
        slow_runner = slow_runner.next

    # Establish the other pointer as fast, moving at a faster rate than the other
        fast_runner = fast_runner.next.next

    # Should these pointers ever meet, return True because we know there's a Cycle
    if fast_runner is slow_runner:
        return True

  # If they don't meet, return False
    return False

  # Runtime for this Algorithm is 0(N) and the Space complexity is 0(1).
