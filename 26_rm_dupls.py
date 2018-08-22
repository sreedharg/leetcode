class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        x = len(nums)
        while i < x:
            if i < x - 1 and nums[i] == nums[i + 1]:
                del nums[i + 1]
                x = len(nums)
            else:
                i = i + 1

        return len(nums)
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1,1,2,3]))
