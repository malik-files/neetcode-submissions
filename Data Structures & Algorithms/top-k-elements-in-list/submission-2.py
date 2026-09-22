class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        frequency = defaultdict(int)

        for x in nums:
            frequency[x] += 1

        uniqueValues = list(set(nums))

        sortedValues = sorted(uniqueValues, reverse=True, key = lambda d: frequency[d])

        return sortedValues[0:k]

