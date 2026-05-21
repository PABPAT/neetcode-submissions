class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        leftPos = 0
        rightPos = len(s) - 1
        while leftPos <= rightPos:
            if not s[leftPos].isalnum():
                leftPos += 1
            elif not s[rightPos].isalnum():
                rightPos -= 1
            elif s[leftPos] == s[rightPos]:
                leftPos += 1
                rightPos -= 1
            else:
                return False
        return True
            
        