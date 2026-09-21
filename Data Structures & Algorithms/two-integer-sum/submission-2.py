class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for x in range(len(nums)):
            i = x
            difference = target - nums[i]
            if difference in nums:
                try:
                    j = nums.index(difference,i+1)
                except:
                    continue
                values = [i,j]
                values.sort()
                return values
            else:
                continue
