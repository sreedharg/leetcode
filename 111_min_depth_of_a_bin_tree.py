# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, depth):
        depth = depth + 1
        if self.min_depth is not None and depth > self.min_depth:
            return
        
        if node.left == None and node.right == None:
            if self.min_depth is None or depth < self.min_depth:
                self.min_depth = depth
            return
        
        if node.left is not None:
            self.traverse(node.left, depth)
            
        if node.right is not None:
            self.traverse(node.right, depth)
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_depth = None
        
        if root is None:
            return 0
        else:
            self.traverse(root, 0)
            return self.min_depth
        