class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        color = [-1 for i in range(n)]
        adj_list = [[] for i in range(n)]
        white = -1
        gray = 0
        black = 1
        
        ans = defaultdict(set)

        for start,end in edges:
            adj_list[end].append(start)

        def dfs(node):
            if not adj_list[node]:
                return
            order = set()
            for child in adj_list[node]:
                if  child not in ans:
                    dfs(child)

                order.add(child)
                order = order | ans[child]
            ans[node] = order



        for i in range(n-1,-1,-1):
            dfs(i)
            
            
        return [sorted(list(ans[i]))  for i in range(n)]

    

