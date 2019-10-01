
def kth_to_last_node(k, head):

    if k < 1:
        raise ValueError('Will not work. Cannot find less than first to last node')

  # Start at 1 to count the head node
    list_length = 1
    current_node = head

  # Traverse the list and increment the list length
    while current_node.next:
        current_node = current_node.next
        list_length += 1

    if k > list_length:
        raise ValueError('Since k is larger than the length of the linked list, this will not work')

    how_far_to_go = list_length - k
    current_node = head

    for i in xrange(how_far_to_go):
        current_node = current_node.next
    return current_node

  # Runtime is Linear O(n) and Space is O(1)





def kth_to_last_node2(k, head):
  # Base case
    if k < 1:
        raise ValueError('Will not work. Cannot find less than first to last node')

  # Establish pointers to start at the head
    left_node = head
    right_node = head

  # Iterate thru the list the right node to be the last node.
    for _ in xrange(k-1):
        if not right_node.next:
            raise ValueError('K is larger than linked list!')

    # Continue iterating
        right_node = right_node.next

  # While we have more ground to cover, keep iterating to the end
    while right_node.next:
        left_node = left_node.next
        right_node = right_node.next

  # Once we reach the end, return left node since we know that's the Kth to the last node.
    return left_node

  # Runtime is Linear O(n) and Space is O(1)

