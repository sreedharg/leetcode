class Solution(object):
    def map_alphabets(self, string):
        s_arr = [0] * 26
        
        for i in string:
            s_arr[ord(i) - ord('a')] += 1
        
        return s_arr
    
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        s_arr = self.map_alphabets(s)
        t_arr = self.map_alphabets(t)
        
        for i in range(26):
            if s_arr[i] != t_arr[i]:
                break

        return chr(i + ord('a'))
