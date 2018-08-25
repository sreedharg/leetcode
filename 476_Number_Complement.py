class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        x = 0
        
        while temp > 0:
            temp = temp >> 1
            x = (x << 1) | 1
           
        return (~num) & x