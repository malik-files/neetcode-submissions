import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        #All the values before i
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i-1] * nums[i-1]
        
        #All the values after i

        for i in range(len(nums) - 1, -1 , -1):
            if i == (len(nums) - 1):
                suffix[i] = 1
            else:
                suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = suffix[i] * prefix[i]

        return result
        

        
        
            
        