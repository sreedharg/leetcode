class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret_val = []
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            y = digits[i] + carry
            if y > 9:
                ret_val.insert(0, y - 10)
                carry = 1
            else:
                ret_val.insert(0, y)
                carry = 0
        
        if carry == 1:
            ret_val.insert(0, 1)
        
        return ret_val
    
sol = Solution()
print(sol.plusOne([0]))