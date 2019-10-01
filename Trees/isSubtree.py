"""
Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree.
A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t.
Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.

"""

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return (root1.value == root2.value and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right))


def isSubtree(t1, t2):
    if t2 is None:
        return True
    if t1 is None:
        return False
    if isIdentical(t1, t2):
        return True
    return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)
