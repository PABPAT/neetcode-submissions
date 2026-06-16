class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm = dict()
        for s in s1:
            hm[s] = hm.get(s, 0) + 1
        
        l = 0
        matched = 0
        for r in range(len(s2)):
            if s2[r] in hm:
                hm[s2[r]] -= 1
                if hm[s2[r]] == 0:
                    matched += 1
            if matched == len(hm):
                return True
            if (r - l + 1) == len(s1):
                if s2[l] in hm:
                    hm[s2[l]] += 1
                    if hm[s2[l]] == 1:
                        matched -= 1
                l += 1
        return False 
            