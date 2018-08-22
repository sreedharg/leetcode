class Solution:
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    res = prices[j] - prices[i]
                    if res > profit: 
                        profit = res
        return profit
          
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = None
        min = None
        profit = 0
                
        for i in prices:
            #print(i, min, max, profit)
            if max is None:
                max = i
            if min is None:
                min = i
            
            if i > max:
                max = i
                if min is not None:
                    if profit == 0 or (max - min) > profit:
                        profit = max - min
            
            if i < min:
                min = i
                
            if i - min > profit:
                profit = i - min
        
        return profit