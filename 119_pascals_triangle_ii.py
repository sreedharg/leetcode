class Solution:
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        prevresult = None
        current = None
        
        for i in range(numRows + 1):
            prevresult = current
            current = [1] * (i + 1)
            
            if i + 1 - 2 > 0:
                for j in range(1,  i):
                    current[j] = prevresult[j - 1] + prevresult[j]
        
        return current
        
sol = Solution()

print(sol.getRow(5))