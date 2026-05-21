class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryNo = bin(n)[2:]
        count = 0
        for i in range(len(binaryNo)):
            if binaryNo[i] == '1':
                count +=1
        return count
        