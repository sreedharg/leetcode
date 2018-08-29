# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, sum, running_sum):
        running_sum += node.val
        #print(running_sum, node.val)
        
        if node.left == None and node.right == None:
            #leaf
            if sum == running_sum:
                return True
            else:
                return False
        
        #print(running_sum, node.val)
        l_stat = False
        r_stat = False
        if node.left is not None:
            l_stat = self.traverse(node.left, sum, running_sum) 
        
        if l_stat is False and node.right is not None:
            r_stat = self.traverse(node.right, sum, running_sum)
        
        return l_stat or r_stat
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        return self.traverse(root, sum, 0)