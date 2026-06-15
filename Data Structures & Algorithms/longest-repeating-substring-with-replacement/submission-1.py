class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        l = 0
        count = [0] * 26
        maxLen = 0
        for r in range(len(s)):
            count [ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, count[ord(s[r]) - ord('A')])
            if (r - l + 1 - maxFreq) > k:
                count[ord(s[l]) - ord('A')] -= 1 
                l += 1
            else:
                 maxLen = max(maxLen, r - l + 1)

        return maxLen
        


        