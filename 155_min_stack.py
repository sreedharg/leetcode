class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.min = None
        
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        node = Node(x)
        if self.head == None:
            node.min = x
            self.head = node
        else:
            if x < self.head.min:
                node.min = x
            else:
                node.min = self.head.min
                
            node.next = self.head
            self.head = node
            
    def pop(self):
        """
        :rtype: void
        """
        val = None
        
        if self.head is not None:
            val = self.head.val
            self.head = self.head.next
        
        return val

    def top(self):
        """
        :rtype: int
        """
        val = None
        
        if self.head is not None:
            val = self.head.val
        
        return val

    def getMin(self):
        """
        :rtype: int
        """
        return self.head.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()