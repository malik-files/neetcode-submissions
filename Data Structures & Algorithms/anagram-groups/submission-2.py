class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) #mapping character count to list of anagrams
        #we can use default dict so each value is a list by default

        for s in strs:
            count = [0] * 26 #so from a to z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return list(result.values())