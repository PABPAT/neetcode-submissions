class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        # Loop through the list to find the max water capacity by checking
        # and calculating at each height.
        while l < r:
            ans = (r-l) * min(heights[l], heights[r])

            res = max(ans, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return res

        