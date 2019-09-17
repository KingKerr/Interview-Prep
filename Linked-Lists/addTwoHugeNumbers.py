"""
You're given 2 huge integers represented by linked lists.
Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits.
The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.


Steps to Solution:

"""
def addTwoHugeNumbers(a, b):
    new_a = reverseList(a)

    new_b = reverseList(b)

    curr_a, curr_b = new_a, new_b

    carry = 0

    new_head = None
    prev = None

    while curr_a is not None or curr_b is not None:
        curr, carry = addLists(curr_a, curr_b, carry)
        if prev:
            prev.next = curr
            prev = curr
        if new_head is None:
            new_head = curr
            prev = curr
        if curr_a:
            curr_a = curr_a.next
        if curr_b:
            curr_b = curr_b.next
    if carry:
        curr = ListNode(carry)
        prev.next = curr
    new_head = reverseList(new_head)

    reverseList(new_a)
    reverseList(new_b)
    return new_head

def addLists(list1, list2, carry = 0):
    if not list1 and not list2 and not carry:
        return None

    list1_val = list1.value if list1 else 0
    list2_val = list2.value if list2 else 0
    total = list1_val + list2_val + carry

    return ListNode(total % 10000), total // 10000


def reverseList(head):
    if head is None:
        return None

    curr, prev = head, None
    while curr is not None:
        temp = curr
        curr = curr.next
        temp.next = prev
        prev = temp
    return prev
