# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        
        prev = None
        next = head.next
        
        if next is None:
            return head
        next2 = None
        if next.next is not None:
            next2 = next.next
        
        while head != None:
            #print(head.val)
            head.next = prev
            if next is not None:
                next.next = head
            prev = head
            head = next
            next = next2
            if next is None:
                continue
                
            if next.next is not None:
                next2 = next.next
            else:
                next2 = None
        
        return prev