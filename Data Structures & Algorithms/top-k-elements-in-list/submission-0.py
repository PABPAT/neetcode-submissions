class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm ={}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in hm.items():
            bucket[freq].append(num)
        
        kElements = []
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                for num in bucket[i]:
                    kElements.append(num)
                    if len(kElements) == k:
                        return kElements



        