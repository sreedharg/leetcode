import unittest


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head, entry=None):
        """
        :type head: Node
        :rtype: Node
        """
        if entry is None:
            entry = True
        currentLocation = head
        tail = None
        
        while currentLocation is not None:
            if currentLocation.child is not None:
                #cache current next
                temp = currentLocation.next
                
                #lift child up
                child_tail = self.flatten(currentLocation.child, False)
                
                currentLocation.next = currentLocation.child
                currentLocation.child.prev = currentLocation
                currentLocation.child = None
                
                #link the cached next to the child level's end
                child_tail.next = temp
                if temp is not None:
                    temp.prev = child_tail
            
            tail = currentLocation
            currentLocation = currentLocation.next
        
        if entry:
            return head
        else:
            return tail
                
class TestSolution(unittest.TestCase):
    def test_flatten(self):
        #build list
        node1 = Node(1)
        child2 = Node(9)
        child = Node(7, child=child2)
        
        node2 = Node(2, prev=node1, child=child)
        node1.next = node2
        
        node = Node(3, prev=node2, next=None)
        node2.next = node
        
        sol = Solution()
        x = sol.flatten(node1)
        
        while x is not None:
            print(x.val)
            x = x.next
            
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)