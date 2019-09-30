"""
Given a Binary Search Tree, find the kth smallest element in it

"""


def kthSmallestInBST(t, k):
    root = t

    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.value
