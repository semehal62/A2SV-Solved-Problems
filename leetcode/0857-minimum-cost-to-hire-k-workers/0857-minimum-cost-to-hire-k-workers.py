class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = []
        for i in range(len(wage)):
            rate = wage[i]/quality[i]
            res.append((rate,quality[i]))

        ans = float("inf")
        res.sort()
        maxheap = []
        totalqual = 0
        for rate,quality in res:
            heappush(maxheap, -quality)
            totalqual += quality

            if len(maxheap) > k:
                totalqual += heappop(maxheap)

            if len(maxheap) == k:
                ans = min(ans,rate* totalqual)

        return ans


