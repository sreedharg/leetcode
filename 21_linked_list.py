# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        a = self
        value = ''
        while a:
            value = value + str(a.val) + '->'
            a = a.next

        return value

class Solution(object):
    def _set_value(self, x):
        if self.head is None:
            self.head = self.tail = ListNode(x.val)
        else:
            self.tail.next = ListNode(x.val)
            self.tail = self.tail.next

    def mergeTwoLists(self, a, b):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.head = None
        self.tail = None

        while a is not None:
            if b is None or a.val < b.val:
                self._set_value(a)
                a = a.next
            else:
                self._set_value(b)
                b = b.next

        while b is not None:
            self._set_value(b)
            b = b.next


        return self.head

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    sol = Solution()
    print(sol.mergeTwoLists(l1, l2))
