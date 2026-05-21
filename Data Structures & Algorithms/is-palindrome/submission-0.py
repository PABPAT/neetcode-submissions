class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        leftPos = 0
        rightPos = len(s) - 1
        while leftPos <= rightPos:
            if s[leftPos].lower() != s[rightPos].lower():
                return False
            else:
                leftPos += 1
                rightPos -= 1
        return True
            
        