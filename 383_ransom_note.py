class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        selected = []
        matched = 0
        
        ransomnote_arr = [0] * 26
        
        #print(ransomnote_arr)
        total = 0
        
        for i, x in enumerate(ransomNote):
            #print(i, x)
            ransomnote_arr[ord(x) - ord('a')] += 1
            total += 1
               
        for j, y in enumerate(magazine):
            #print(j, y)
            if ransomnote_arr[ord(y) - ord('a')] > 0:
                ransomnote_arr[ord(y) - ord('a')] -= 1
                total -= 1
                if total == 0:
                    break
        
        if total == 0:
            return True
        else:
            return False
   