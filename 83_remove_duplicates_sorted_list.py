#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur_item = head
        
        while cur_item is not None:
            while cur_item.next is not None and cur_item.val == cur_item.next.val:
                cur_item.next = cur_item.next.next
            cur_item = cur_item.next
            
        return head
    
a = ListNode(1)
b = ListNode(1)
a.next = b
c = ListNode(1)
b.next = c
d = ListNode(1)
c.next = d
e = ListNode(1)
d.next = e

sol = Solution()

item = sol.deleteDuplicates(a)

while item:
    print(item.val, '->')
    item = item.next