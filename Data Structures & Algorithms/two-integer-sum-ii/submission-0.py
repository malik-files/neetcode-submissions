class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for value in numbers:
            if (target - value) in numbers:
                firstValueIndex = numbers.index(value)
                secondValueIndex = numbers.index(target-value, firstValueIndex)
                return [firstValueIndex+1, secondValueIndex+1]
