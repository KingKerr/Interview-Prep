"""
Give an algorithm that traverses a Binary Tree in Zigzag order. An example is as follows:

          1
        /   \
       2     3
      / \  /  \
     4   5 6    7

The output here should be: 1, 2, 3, 4, 5, 6, 7

"""

def zigZagTraversal(self, root):
    result = []

    currentLevel = []

    if root != None:
        currentLevel.append(root)

    LeftToRight = True

    while len(currentLevel) > 0:
        levelResult = []
        nextLevel = []
        while len(currentLevel) > 0:
            node = currentLevel.pop()
            levelResult.append(node.val)
            if LeftToRight:
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
            else:
                if node.right != None:
                    nextLevel.append(node.right)
                if node.left != None:
                    nextLevel.append(node.left)
        currentLevel = nextLevel
        result.append(levelResult)
        LeftToRight = not LeftToRight
    return result

"""
Time Complexity: O(N)
Space Complexity: O(N)

"""

