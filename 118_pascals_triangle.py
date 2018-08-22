class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [None] * numRows
        for i in range(numRows):
            res = [1] * (i + 1)
            
            if i + 1 - 2 > 0:
                for j in range(1,  i):
                    res[j] = result[i - 1][j - 1] + result[i - 1][j]
                    
            result[i] = res
        
        return result
    
sol = Solution()

print(sol.generate(5))