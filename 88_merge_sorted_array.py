class Solution:
    def shift(self, nums1, j, final_len):
        for i in range(final_len, j, -1):
            nums1[i] = nums1[i - 1]

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
    
        ptr = 0
        final_len = m
        
        for i in range(len(nums2)):
            
            for j in range(ptr, len(nums1)):
                #print(nums1, nums2, nums2[i], nums1[j], ptr, final_len, j)
                if nums2[i] < nums1[j]:
                    #shift array
                    self.shift(nums1, j, final_len)
                    nums1[j] = nums2[i]
                    ptr = j
                    final_len += 1
                    break
                    
                if j == final_len:
                    nums1[j] = nums2[i]
                    j = ptr
                    final_len += 1
                    break
                    
        return nums1

sol = Solution()

print(sol.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))
