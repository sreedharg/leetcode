class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_val = None
        max_val = None
        
        for i in prices:
        #    print(i, min_val, max_val, profit)
        # if first, then register it is min_val
            if min_val is None:
                min_val = max_val = i
                continue
                
        # if greater than the previous store it as max_val, but continue
            if i >= max_val:
                max_val = i
        # if lesser than the previous
            else:
                if max_val > min_val:
        # calculate profit as max_val - min_val  
                    profit += max_val - min_val
                min_val = i
        # store it as the new min_val
        # initialize max_val
                max_val = i
        
        if max_val is not None and max_val > min_val:
            profit += max_val - min_val
        return profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([1,2,3,4,5]))
print(sol.maxProfit([7,6,4,3,1]))