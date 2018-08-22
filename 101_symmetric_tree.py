# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None:
            if q is None:
                return True
            else:
                return False
        elif q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)    
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isSameTree(root.left, root.right)
        