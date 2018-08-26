class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        for i in sorted(nums):
            #print(i, prev)
            if prev is None:
                prev = i
            elif i != prev:
                break
            else:
                prev = None
        
        return prev
