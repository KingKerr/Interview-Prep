"""
Given a Binary Tree t and an integer s, determine whether there is a root to leaf path in t,
such that the sum of vertex equals s.
Here's t:
              4
            /   \
           1     3
          /     / \
        -2     1   2
          \       / \
          -3    -2  -3

s = 7

Path 4 --> 3 --> 2 --> -2 will total 7 so we return true

"""

def hasPathWithGivenSum(t, s):

    if t is None:
        if s == 0:
            return True
        else:
            return False

    else:
        answer = False
        subSum = s - t.value

        if subSum == 0 and t.left is None and t.right is None:
            return True

        if t.left is not None:
            answer = answer or hasPathWithGivenSum(t.left, subSum)

        if t.right is not None:
            answer = answer or hasPathWithGivenSum(t.right, subSum)

        return answer
