class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        found = False
        
        for x in range(len(numbers)):
            if numbers[x] > target:
                break
        
        prev = None
        
        for i in range(x + 1):
            if prev is None:
                prev = numbers[i]
            else:
                while i < (x + 1) and prev == numbers[i]:
                    prev = numbers[i]
                    i = i + 1
                if i == (x + 1):
                    break
                    
            for j in range(i + 1, x + 1):
                cur_sum = numbers[i] + numbers[j]
                if cur_sum == target:
                    result.append(i + 1)
                    result.append(j + 1)
                    found = True
                    break
                elif cur_sum > target:
                    break
            if found:
                break
                
        return result

sol = Solution()
print(sol.twoSum([-1,0], -1))
