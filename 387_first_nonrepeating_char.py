class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_loc = [-1] * 26
        count_flags = [0] * 26
        #print(unique_flags)
        
        for i, x in enumerate(s):
            #print(i, x, ord(x), ord('a'))
            count_flags[ord(x) - ord('a')] += 1
            first_loc[ord(x) - ord('a')] = i
            
        result = -1
        
        for i, data in enumerate(count_flags):
            #print(i, data, first_loc[i])
            if data == 1:
                if result == -1 or first_loc[i] < result:
                    result = first_loc[i]
                
        
        return result
    