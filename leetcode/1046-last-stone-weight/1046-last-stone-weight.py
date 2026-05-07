class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapify(stones)

        while len(stones) > 1:
            num1 = - heappop(stones)
            num2 = - heappop(stones)
            num1 = num1 - num2
            heappush(stones,-num1)

        return - stones[0]
