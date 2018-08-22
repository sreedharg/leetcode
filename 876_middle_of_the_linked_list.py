# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        counter = 0
        middle = head
        
        while curr is not None:
            counter += 1
            if counter % 2 == 0:
                middle = middle.next
                
            curr = curr.next
            
        return middle