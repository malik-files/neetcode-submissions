class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = list()
        sizeOfList = len(nums)
        for x in range(sizeOfList):
            tempResult = 1
            for y in range(sizeOfList):
                if y == x:
                    continue
                tempResult = nums[y] * tempResult
            results.append(tempResult)
        return results