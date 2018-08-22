class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        start = False
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                start = True
                j += 1
            elif start is True and s[i] == ' ':
                break
        
        if start is True:
            return j
        
        return 0
            

sol = Solution()
sol.lengthOfLastWord(" ")