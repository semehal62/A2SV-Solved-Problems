class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        visted = [-1] * (n + 1)
        adj_list = [[] for i in range(n)]

        for pre,nexts in relations:
            adj_list[pre-1].append(nexts)

        def dfs(node):
            if visted[i] >= 0:
                return visted[i]

            maxi = 0
            for neb in adj_list[node-1]:
                if visted[neb] < 0:
                    dfs(neb)          
             
                maxi = max(maxi,visted[neb])

            visted[node] = time[node-1] + maxi
            return visted[node]



        for i in range(1,n+1):
             dfs(i)
               
        return max(visted)


            


