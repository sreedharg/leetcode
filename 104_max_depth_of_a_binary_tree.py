import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        while root is not None:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        
        return 0
    
class TestSolution(unittest.TestCase):
    def testMaxDepth(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        sol = Solution()
        maxdepth = sol.maxDepth(root)
        self.assertEqual(maxdepth, 3)

    def testMaxDepthSingleNode(self):
        root = TreeNode(3)

        sol = Solution()
        maxdepth = sol.maxDepth(root)
        self.assertEqual(maxdepth, 1)

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
        