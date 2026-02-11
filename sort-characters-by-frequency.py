class Solution:
    def frequencySort(self, s: str) -> str:
        letters = Counter(s)

        coll = sorted(letters.items(),key = lambda x: (-x[1],x[0]))
        
        ans = ""

        for letter, freq in coll:
            ans += letter * freq

        return ans
