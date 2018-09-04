# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        temp2 = head
        
        cycle_found = False
        
        while True:
            if temp is None or temp2 is None:
                break
            
            temp = temp.next
            if temp2.next is None:
                break
                
            temp2 = temp2.next.next
            
            if temp == temp2:
                cycle_found = True
                break
        
        return cycle_found
    