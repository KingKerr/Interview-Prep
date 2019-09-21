"""
Pre-order Traversal.. We will start off with the Root node and then traverse
to the Left subtree and then to the Right subtree.

"""

def preOrderTraversal(self, root):
    if root is None:
        return None:

    final, stack = [], [root]

    while stack:
        node = stack.pop()
        if node:
            final.append(root.value)
            stack.append(right.value)
            stack.append(left.value)
    return final

"""
Runtime is O(N) and Space is O(N)

"""
