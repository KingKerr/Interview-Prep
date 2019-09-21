"""
In-Order Traversal.. This means we will traverse the tree's Left subtree first,
then move to the Root node and then the Right subtree.

"""

def inOrderTraversal(self, root):
    if root is None:
        return None:
    # False will denote if we've visited this node or not
    final, stack = [], [(root, False)]

    while stack:
        node, visited = stack.pop()
            if node:
                if visited:
                    final.append(node.value)
                else:
                    stack.append((node.right, False))
                    stack.append((node.value, True))
                    stack.append((node.value, False))
    return final

"""
Runtime is O(N) and Space is O(N)

"""
