class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCapacity = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            maxCapacity = max((min(heights[l], heights[r]) * (r - l)), maxCapacity)
            if heights[l] < heights[r]:
                l +=1
            elif heights[r] < heights[l]:
                r -=1
            else:
                l +=1
        return maxCapacity
        