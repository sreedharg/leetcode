# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor = 2
        val = n - n // factor
        x = 100
        
        while True:
            factor = factor * 2
            diff = n // factor
            if diff == 0:
                diff = 1
                
            print(val, x)
            x = guess(val)
            if x == 0:
                return val
            elif x == 1:
                val = val + diff
            else:
                val = val - diff
                