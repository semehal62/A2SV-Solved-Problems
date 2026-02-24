class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i in range(len(s)):
            last[s[i]] = i
        
        max_last = 0
        prev = -1
        ans = []
        for i in range(len(s)):
            max_last = max(max_last, last[s[i]])
            if i == max_last:
                ans.append(i - prev)
                prev = i
        return ans




        
