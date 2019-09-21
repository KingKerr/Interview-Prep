"""
Post-Order Traversal.. Means you will traverse the Left subtree first,
then the Right subtree and then the Root node last..

"""

def postOrderTraversal(self, root):
    if root is None:
        return None

    final, stack = [], [(root, False)]

    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                final.append(node.value)
            else:
                stack.append((node.value, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return final

"""
Runtime is O(N) and Space is O(N)

"""
