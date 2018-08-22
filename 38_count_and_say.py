class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n_str = '1'
        out_str = ''
        
        #print(n_str)
        for i in range(n-1):
            count = 0
            prev = ''
            for j, c in enumerate(n_str):
                if j == 0 or c == prev:
                    count += 1
                else:
                    out_str += str(count) + prev
                    count = 1
                prev = c
            out_str += str(count) + prev
            #print(out_str)
            n_str = out_str
            out_str = ''
        
        return(n_str)
    
sol = Solution()
print(sol.countAndSay(1))