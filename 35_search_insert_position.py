#Given a sorted array and a target value, return the index if the target is found. If not, return the index 
#where it would be if it were inserted in order.
#You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self._nums = nums
        self._target = target
        if len(nums) == 0:
            return 0

        return self.findPos(0, len(nums) - 1)

    def findPos(self, low, high):
        #print(low, high, nums[low:high + 1])
        if low >= high:
            if self._target <= self._nums[low]:
                return low
            else:
                return low + 1

        mid = (low + high) // 2

        if self._target == self._nums[mid]:
            return mid
        elif self._target < self._nums[mid]:
            return self.findPos(low, mid - 1)
        else: 
            return self.findPos(mid + 1, high)

                
sol = Solution()
res = sol.searchInsert([1,3], 0)
print(res)            