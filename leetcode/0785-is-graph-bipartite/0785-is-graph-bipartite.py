class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        arr = [5] * len(graph)
        n = len(graph)

        color = 0
        def dfs(m):
            temp = True
            for num in graph[m]:
                if arr[num] == 5:
                    if arr[m] == 0:
                        arr[num] = 1
                    else:
                        arr[num] = 0
                    temp = temp and dfs(num)
                elif arr[num] == arr[m]:
                    return False
            return temp

        for i in range(n):
            if arr[i] == 5:
                arr[i] = color
            if  not dfs(i):
                return False

        return True
        