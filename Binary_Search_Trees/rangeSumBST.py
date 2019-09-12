"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

"""

def rangeSumBST(self, root, L, R):
    # This variable keeps track of our running sum
    range_sum = 0

    # This variable will keep track of where we are in BST, starting at root obviously
    current_node = root

    # Base case.. If nothing is here just return 0
    if not current_node:
        return 0

    # Begin traversal of BST
    # Is the value within our current bounds?
    if current_node.val >= L and current_node <= R:
        range_sum += current_node.val

    if current_node.val > L:
        range_sum += self.rangeSumBST(root.left, L, R)

    if current_node.val < R:
        range_sum += self.rangeSumBST(root.right, L, R)

    return range_sum
