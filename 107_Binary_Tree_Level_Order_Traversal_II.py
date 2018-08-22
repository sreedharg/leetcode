# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        bfsq = []
        if root is not None:
            bfsq.insert(0, (root, 0))
        
        while (len(bfsq) > 0):
            item, level = bfsq.pop()
            #print(item.val, level)
            
            if len(result) < level + 1:
                result.insert(0, [item.val])
            else:
                result[0].append(item.val)
            
            if item.left is not None:
                bfsq.insert(0, (item.left, level + 1))
            
            if item.right is not None:
                bfsq.insert(0, (item.right, level + 1))

        #result.reverse()
        
        return result