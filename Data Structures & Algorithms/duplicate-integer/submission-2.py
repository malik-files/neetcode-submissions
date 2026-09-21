class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfSeenNumbers = set()
        for x in nums:
            if x in setOfSeenNumbers:
                return True
            else:
                setOfSeenNumbers.add(x)
            
        return False