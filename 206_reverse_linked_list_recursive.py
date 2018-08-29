# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def traverse(self, current, prev):
        #print(current.val)
        #if prev is not None:
        #    print('--', prev.val)
        temp = current.next
        current.next = prev
        
        if temp is None:
            return current
        else:
            return self.traverse(temp, current)
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        return self.traverse(head, None)
        
        
        
        