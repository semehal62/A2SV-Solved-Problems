class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj_list = [[] for i in range(len(quiet))]
        for a,b in richer:
            adj_list[b].append(a)

        ans = [-1] * len(quiet)
        def dfs(person):
            if ans[person] >= 0:
                return

            mini = [quiet[person],person]
            for i in adj_list[person]:
                if ans[i] < 0:
                    dfs(i)

                if mini[0] > quiet[ans[i]]:
                    mini[0] = quiet[ans[i]]
                    mini[1] = ans[i]

            ans[person] = mini[1]
           
            

        for i in range(len(quiet)):
            dfs(i)

        return ans