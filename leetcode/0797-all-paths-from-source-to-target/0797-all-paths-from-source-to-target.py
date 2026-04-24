class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        res = set()

        def dfs(i,arr):
            if i == n and arr:
                res.add(tuple(arr[:]))
                return 

            for num in graph[i]:
                    arr.append(num)
                    dfs(num,arr)                       
                    arr.pop()
                   
                
        dfs(0,[0])
        return list(res)