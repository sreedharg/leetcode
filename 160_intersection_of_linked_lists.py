# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLen(self, node):
        length = 0
        
        while node is not None:
            node = node.next
            length += 1
        
        return length
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)
        
        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        else:
            for _ in range(lenB - lenA):
                headB = headB.next
        
        result = None
        
        while headA is not None:
            if headA == headB:
                result = headA
                break
                
            headA = headA.next
            headB = headB.next
            
        return result