class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        alphas = 'abcdefghijklmnopqrstuvwxyz01234567890'
        
        match = False
        alphaFound = False
        
        while i < j:
            a = s[i].lower()
            #print(a, b)
            if a not in alphas:
                i += 1
                continue
                
            b = s[j].lower()
                
            if b not in alphas:
                j -= 1
                continue
            
            alphaFound = True
            
            if a != b:
                return False
            
            match = True
            
            i += 1
            j -= 1
        
        if match is True or alphaFound is False:
            return True
        else:
            return False
    
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome("0P"))
print(sol.isPalindrome("  "))