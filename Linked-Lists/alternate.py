"""
Given a linked list, rearrange the node values so that they appear
in alternating form, such as low --> high --> low --> high
"""

"""
Solution --
"""

def alternate(L):

  # First establish 2 pointers
  # We will track the current node and the one after it
  prev = L
  curr = L.next

  # Begin List traversal
  while curr:
    if prev.data > curr.data: # If the previous node is greater than the current node
      prev.data, curr.data = curr.data, prev.data # Swap them

    if not curr.next: # If we don't have anywhere else to go, let's break here.
      break

    # If the next node is greater than the current node
    if curr.next.data > curr.data:
      curr.next.data, curr.data = curr.data, curr.next.data # Swap them

    # Update the pointers so we're jumping a couple spots ahead and we can continue our comparisons
    prev = curr.next
    curr = curr.next.next

  # Once we're done traversing, return the Linked List
  return L

  # This uses 0(N) runtime since we're traversing the entire list and 0(1) space
