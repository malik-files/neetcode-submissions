class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1
        listOfLength = list()
        nums.sort()
        nums = list(OrderedDict.fromkeys(nums))
        print(f"The nums are {nums}")
        for index in range(len(nums)):
            if index == len(nums) - 1:
                listOfLength.append(length)
                break
            if nums[index+1] == nums[index] + 1:
                length += 1
            else:
                length = 1    
            listOfLength.append(length)
            
        
        listOfLength.sort(reverse=True)
        print(f"The list is {listOfLength}")
        if len(listOfLength) == 0 :
            return 0
        else:
            return listOfLength[0]
        
            
            
        