class Solution:
    def __init__(self):
        self.memory = {}
        
    def findCount(self, i, n):
        if i > n or n == 0:
            return 0
        
        if n == i:
            return 1
        
        if i in self.memory:
            #print('found -- ', i, self.memory[i])
            return self.memory[i]
        
        self.memory[i] = self.findCount(i + 1, n) + self.findCount(i + 2, n)
        #print(self.memory[i], i)
        return self.memory[i]
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return self.findCount(0, n)
    
    def climbStairsDynamic(self, n):
        res = {}
        
        if n == 1:
            return 1
        
        if n == 0:
            return 0
        
        res[1] = 1
        res[2] = 2
        
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res [i - 2]
        
        return res[n]
        
sol = Solution()
%timeit sol.climbStairs(10)
%timeit sol.climbStairsDynamic(10)
