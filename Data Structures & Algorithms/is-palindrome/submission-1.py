import re
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        newText = str()
        for char in s:
            if char.isalnum():
                newText += char
        print(newText)

        if newText == newText[::-1]:
            return True
        else:
            return False