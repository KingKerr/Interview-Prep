# Find the intersecting nodes of two linked lists

# First we'll write a helper function so we can get the length of the lists.

def length(head):
    if not head:
        return 0

    return 1 + length(head.next)



# Next we'll write an algorithm to find out where the lists intersect.

def intersecting_nodes(a, b):

  # Calculate the length of both lists
    m, n = length(a), length(b)

  # Establish both pointers
    curr_a, curr_b = a, b

  # If M is longer than N,
    if m > n:
    # Iterate thru the larger list by the difference
        for _ in range(m-n):
            curr_a = curr_a.next
  # If N is longer than M
    else:
    # Iterate thru the larger list by the difference
        for _ in range(n-m):
            curr_b = curr_b.next

  # While we don't have a match
    while curr_a != curr_b:
    # Keep iterating both pointers
        curr_a = curr_a.next
        curr_b = curr_b.next
  # Once we do, return a pointer
    return curr_a
