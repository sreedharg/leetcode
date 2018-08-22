class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result_len = 0
        result_str = ''

        if len(strs) == 1:
            return strs[0]
        
        # get the smallest str

        min_len = None
        smallest_str = None

        for item in strs:
            l = len(item)
            if min_len is None:
                min_len = l
                smallest_str = item
            elif l < min_len:
                min_len = l
                smallest_str = item
        
        for item in (strs):
            match_len = 0
            for i in range(min_len):

                if item[i] == smallest_str[i]:
                    match_len = match_len + 1
                else:
                    break

            if match_len == 0:
                result_str = ''
                break
            else:
                if match_len < min_len:
                    min_len = match_len
                result_str = item[:min_len]

        return result_str

if __name__ == '__main__':
    sol = Solution()

    strs = ['hello', 'hakjkaj', 'll']
    print(sol.longestCommonPrefix(strs))

    strs = ['ahello', 'hellg', 'hello']
    print(sol.longestCommonPrefix(strs))

    strs = ['c', 'c']
    print(sol.longestCommonPrefix(strs))

                    

        
