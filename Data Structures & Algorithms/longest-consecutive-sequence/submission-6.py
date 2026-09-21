class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 :
            return 0

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
                listOfLength.append(length)
                length = 1    
                
            
        
        listOfLength.sort(reverse=True)
        print(f"The list is {listOfLength}")

        
        return listOfLength[0]
        
            
            
        