class Solution:
    def findValidPair(self, s: str) -> str:
        count_num = Counter(s)
        for i in range(len(s)-1):
            pairs = s[i:i+2]
            if count_num[pairs[0]]  == int(pairs[0]) and count_num[pairs[1]]  == int(pairs[1]) and pairs[0] != pairs[1]:
                return pairs

        return ""
