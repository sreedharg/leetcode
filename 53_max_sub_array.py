class Solution(object):
    def maxSubArrayBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = float("-inf")
        max_array = []
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                print(nums[j: j + i + 1])
                s = sum(nums[j:j+i + 1])
                if s > max:
                    max = s
                    #max_array = nums[j:j+i]
        return(max)
    
    def maxSubArray(self, nums):
        maxn = max_ending_here = nums[0]
        
        for x in nums[1:]:
            maxn += x
            
            if maxn < x:
                maxn = x
                    
            #print(maxn, max_ending_here)
            if maxn > max_ending_here:    
                max_ending_here = maxn
            
        return max_ending_here
        
    
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([-1, -2]))
             