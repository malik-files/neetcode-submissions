class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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