"""
Level-Order Traversal for a Binary Tree. We'll start at the Root node and then
traverse each level and visit all nodes at that level. This will be repeated until
all levels have been done.

"""

def levelOrderTraversal(self, root):
    if root is None:
        return None
    final, queue = [], [root]
    while queue:
        new_queue = []
        final.append([n.value for n in queue])
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue
    return final


"""
Runtime is O(N) and Space is O(N)

"""
