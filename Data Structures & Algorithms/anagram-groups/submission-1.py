class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Use the dictionary
        "Lists are mutable in python so I need an immutable item to use 
        as my key so use a tuple.
        '''
        # def sortedWord(word):
        #     sortedWord = sorted(word)
        #     newWord = str()
        #     for x in sortedWord:
        #         newWord = newWord + x

        #     return x

        wordMap = dict()

        for x in strs:
            tupleX = tuple(sorted(x))
            wordMap[tupleX] = wordMap.get(tupleX, list()) + [x]
        
        returnList = list()

        for word in wordMap:
            returnList.append(wordMap[word])

        return returnList
