"""
Given a binary tree t, determine if it is symmetric around its center, i.e. each side
mirrors the other

"""

def isTreeSymmetric(self, t):
    if t is None:
        return True

    root = t
    stack = [[root.left, root.right]]

    while len(stack) > 0:
        node = stack.pop()
        leftSubtree = node[0]
        rightSubtree = node[1]

        if leftSubtree is None and rightSubtree is None:
            continue
        # Cannot be symmetric if one is None
        if leftSubtree is None or rightSubtree is None:
            return False
        # If value is the same, append both right and left to each
        if leftSubtree.value == rightSubtree.value:
            stack.append([leftSubtree.left, rightSubtree.right])
            stack.append([leftSubtree.right, rightSubtree.left])
        # If not, we know it is False
        else:
            return False
    return True

"""
Runtime is O(N) since we're going through the entire Tree.

Space is O(N) since we're using an empty array to store everything.
