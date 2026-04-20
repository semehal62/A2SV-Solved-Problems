class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        arr = ["a", "b", "c"]
        res = []
        curr = []
        
        def backtracking(idx,prev):
            if idx == n:
                res.append("".join(curr[:]))
                return 
            for option in arr:
                if option != prev:
                    curr.append(option)
                    backtracking(idx + 1,option)
                    curr.pop()

  

            
        backtracking(0,-1)
        if k <= len(res):
            return res[k-1]
        else:
            return ""


