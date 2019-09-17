"""
Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].

Steps to solution:

1.) First, Set up base cases. Establish a new List too.

2.) Begin traversal, compare the values of the heads of both lists. Whichever the lesser is, set that to be the head node in the new List.

    Continue traversal.

3.) return the new List.next

"""

def mergeTwoLinkedLists(l1, l2):

    head1 = l1
    head2 = l2
    # Base cases
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1 is None and head2 is None:
        return None

    # Establish a new list
    L3 = ListNode(None)

    current = L3
    # Begin traversal
    while head1 and head2:
        # Establish which is the smaller node
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        # Continue iterating
        current = current.next
    # Once done, if there's a non-empty list set it here
    current.next = head1 or head2

    # Return New List's next
    return L3.next
