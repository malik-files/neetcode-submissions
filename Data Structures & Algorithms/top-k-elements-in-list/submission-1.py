class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def counter(s):
            return nums.count(s)

        listOfValues = list(OrderedDict.fromkeys(nums))

        listOfValues.sort(reverse=True, key=counter)

        return listOfValues[0:k]