class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for x in range(len(nums)):
            if (target - nums[x]) in hm:
                return [hm[target-nums[x]], x]
            else:
                hm[nums[x]] = x
        return []
        