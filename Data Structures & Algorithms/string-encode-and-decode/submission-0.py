class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeString = ""
        for s in strs:
            encodeString += str(len(s)) + "#" + s
        return encodeString

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            i = j + 1 + length
            result.append(word)
        return result

