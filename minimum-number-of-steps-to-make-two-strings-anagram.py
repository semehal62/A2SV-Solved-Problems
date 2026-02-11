class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_t = Counter(t)
        count_s = Counter(s)
        count = 0
        for key,val in count_t.items():
            if key not in count_s:
                count += val
            elif val > count_s[key]:
                count += val - count_s[key]

        
        return count
