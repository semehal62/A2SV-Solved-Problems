class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        dp = defaultdict(lambda:False)
        dp[0] = True
        arr = []
        def recur(i):
            if i == len(s)+1:
                res.append(" ".join(arr[:]))
                return
            
            for j in range(i,len(s)+1):
                for word in wordDict:
                    if j- len(word) >= i-1 and dp[j-len(word)] and s[j-len(word):j] == word:
                        arr.append(word)
                        dp[j] = True
                        recur(j+1)
                        arr.pop()
                        dp[j] = False

                









        recur(1)

        return res