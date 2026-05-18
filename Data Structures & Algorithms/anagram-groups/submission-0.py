class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for x in strs:
            key = ''.join(sorted(x))
            if key not in hm:
                hm[key]= []
            hm[key].append(x)
        return list(hm.values())
        