class Solution:
    def trap(self, height: List[int]) -> int:
        l_maxHeight = {}
        r_maxHeight = {}
        totalWater = 0

        # Find max height for left of each element
        currMax = height[0]
        l_maxHeight[0] = 0
        for i in range(1, len(height)):
            if height[i] > currMax:
                currMax = height[i]
            l_maxHeight[i] = currMax

        # Find max height for right of each element
        currMax = height[- 1]
        r_maxHeight[len(height)- 1] = 0

        for i in range(len(height) - 2, -1, -1):
            if height[i] > currMax:
                currMax = height[i]
            r_maxHeight[i] = currMax
        
        for i in range(len(height)):
            curRes = min(l_maxHeight[i],r_maxHeight[i]) - height[i]

            if curRes > 0:
                totalWater += curRes
        
        return totalWater

        