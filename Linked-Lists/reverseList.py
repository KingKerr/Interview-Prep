# Reverse a singly-linked list in-place

def reverse(L):
  # Here we establish two pointers.
  # One is at the head and the other prev follows one node behind it
    prev = None
    current = L.head

  # Next we traverse the list starting at the head
    while current is not None:
    # Identify the node that's ahead of current
        next_node = current_next
    # Point that that node behind the current
        current_next = prev
    # Move the two pointers forward
        prev = current
        current = next_node
  # Return that last node
    return prev

  # Runtime is going to be O(n) due to the fact we're iterating through the entire list.
  # Space is going to be O(1) since this is being done in-place
