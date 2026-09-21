class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for value in numbers:
            difference = target - value
            if difference in numbers:
                firstValueIndex = numbers.index(value)
                secondValueIndex = numbers.index(difference, firstValueIndex)
                return [firstValueIndex+1, secondValueIndex+1]
