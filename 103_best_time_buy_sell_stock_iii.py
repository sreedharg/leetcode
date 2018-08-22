class Solution:
    def storeProfit(self, profit):
        print(self.profits, profit)
        store_idx = -1
        min = None
        print(self.profits)
        for i, val in enumerate(self.profits):
            if min is None:
                min = val
                store_idx = i
                
            if val == 0:
                self.profits[i] = profit
                return
            elif val < min:
                store_idx = i
                min = val
        
        if store_idx > -1 and profit > self.profits[store_idx]:
            self.profits[store_idx] = profit
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.profits = [0, 0]
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
                    profit = max_val - min_val
                    self.storeProfit(profit)
                
                min_val = i
        # store it as the new min_val
        # initialize max_val
                max_val = i
        
        if max_val is not None and max_val > min_val:
            profit = max_val - min_val
            self.storeProfit(profit)
        
        print(self.profits)
        return sum(self.profits)


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([1,2,3,4,5]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([3,3,5,0,0,3,1,4]))
print(sol.maxProfit([6,1,3,2,4,7]))
print(sol.maxProfit([1,2,4,2,5,7,2,4,9,0]))