class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnList = list()
        if len(strs) == 0:
            returnList.append(list())
            return returnList
        


        def isItAnAnagram(s,t):
            s = list(s)
            t = list(t)
            setOfCharacters = set(s)

            if len(s) != len(t):
                return False
            else:
                for x in setOfCharacters:
                    if s.count(x) != t.count(x):
                        return False
                return True
            
        while len(strs) > 0:
            x = strs[0]
            print(x)
            temporaryList = [x]
            strs.remove(x)
            for y in strs:
                if isItAnAnagram(x,y):
                    temporaryList.append(y)
            for z in temporaryList:
                if z in strs:
                    strs.remove(z)
                    
            returnList.append(temporaryList)
        
        return returnList
            

        