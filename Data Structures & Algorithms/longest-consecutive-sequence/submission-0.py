class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        digits = set(nums)
        longest = 0

        for num in digits:
            if num - 1 not in digits:
                length = 1
                while num + 1 in digits:
                    num += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
        