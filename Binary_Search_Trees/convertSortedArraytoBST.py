"""
Take a sorted array and convert to a Binary Search Tree

"""
class Node:
    def __init__(self, data, left = None, right = None):
        self.data
        self.left = left
        self.right = right

def makeBST(array):
    # Establish base case
    if not array:
        return None

    # Since array is sorted, the middle array can actually be our root node of BST
    mid = len(array) // 2
    # Establish root node
    root = Node(array[mid])

    # Left subtree will be everything that's less/to the left of the root
    root.left = makeBST(array[:mid])

    # Right subtree is everything that's more/to the right of the root
    root.right = makeBST(array[mid + 1])

    # Return our root node which will have both the established left subtree and right subtree
    return root
