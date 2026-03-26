class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        res = []
        def recur(n,k,j):
            if len(arr) == k:
                res.append(arr[:])
                return 
            
           
            for i in range(j, n+1):
                arr.append(i)
                recur(n,k,i+1)
                arr.pop()
            
        recur(n,k,1)
        
        return res