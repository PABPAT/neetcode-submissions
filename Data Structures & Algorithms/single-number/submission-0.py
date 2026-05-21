class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unqNo = 0
        for num in nums:
            unqNo ^= num
        return unqNo
        