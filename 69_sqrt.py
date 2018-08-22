import math

class Solution(object):
    def findsqrt(self, x, low, high):

        mid = (low + high) / 2        

        if abs(mid * mid - x) < 1:
            rmid = math.ceil(mid)
            y = rmid * rmid
            if y == x:
                return rmid
            else:
                return math.floor(mid)

        res = mid * mid            

        #print(x, mid, res, abs(mid * mid - x), low, high)
        
        if res == x:
            return mid
        elif res > x:
            return self.findsqrt(x, low, mid)
        else:
            return self.findsqrt(x, mid, high)
        
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #return int(math.sqrt(x))
        return self.findsqrt(x, 0, x)

sol = Solution()
#print(sol.mySqrt(8))
%timeit sol.mySqrt(2147395599)
%timeit int(math.sqrt(2147395599))