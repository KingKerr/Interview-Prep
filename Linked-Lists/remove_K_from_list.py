"""
Given a singly linked list of integers, remove all elements from the linked list
that have  value equal to k.

"""

def remove_K_from_list(l, K):

  # Establish a new node
  head = ListNode(None)

  # Establish that new node's 'next' pointer
  head.next = l

  # Set a variable for the new node
  current = head

  # Begin traversal
  while current:
    # While we have a value that's equal to K
    while current.next and current.next.value == K:
      # Update pointer to be the next, next pointer
      current.next = current.next.next

    # If not equal to K, just keep iterating.
    current = current.next

  # Return that list once done
  return head.next


# Runtime is 0(N) and the Space complexity is 0(1).
