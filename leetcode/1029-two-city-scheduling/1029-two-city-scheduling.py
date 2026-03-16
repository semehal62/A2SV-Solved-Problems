class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: ( (x[0] - x[1]),-x[1] ))
        ans = 0
        n = len(costs) // 2
        for i in range(len(costs)):
            a,b = costs[i]
            if i < n:
                ans += a
            else:
                ans += b

        return ans

        

        