class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm ={}
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        for num, freq in hm.items():
            bucket[freq].append(num)
        
        kElements = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                kElements.append(num)
                if len(kElements) == k:
                    return kElements



        