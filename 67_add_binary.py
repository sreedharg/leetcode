class Solution(object):
    def addFunc(self, x, y, carry):
        #print('addFunc ', x, y, carry)
        res = '0'
        nextcarry = False
        
        if x == '0' and y == '1' or x == '1' and y == '0':
            res = '1'
            if carry:
                res = '0'
                nextcarry = True
        elif x == '1' and y == '1':
            res = '0'
            nextcarry = True
            if carry:
                res = '1'
                nextcarry = True
        else:
            if carry:
                res = '1'
                nextcarry = False
            
        
        return res, nextcarry
    
    def addStrings(self, a, b):
        res_str = ''
        carry = False
        
        j = len(b) - 1
                
        for i in range(len(a) - 1, -1, -1):
            #print(res_str)
            if j >= 0:
                res, carry = self.addFunc(a[i], b[j], carry)
                j -= 1        
            else:
                if carry:
                    res, carry = self.addFunc(a[i], '1', False)
                else:
                    res, carry = self.addFunc(a[i], '0', False)
                
            res_str = res + res_str
        
        if carry:
            res_str = '1' + res_str
            
        #print(carry)
        return res_str
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alen = len(a)
        blen = len(b)
        
        if alen > blen:
            return self.addStrings(a, b)
        else:
            return self.addStrings(b, a)
            
        
                    
sol = Solution()
print(sol.addBinary('1', '111'))
print(sol.addBinary('1010', '1011'))