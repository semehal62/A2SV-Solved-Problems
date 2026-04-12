class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        h = max(candies)
        def checker(cap):
            count = 0
            for i in range(len(candies)):
               count += candies[i] // cap

            return count >= k
        
        while l <= h:
            mid = (l + h)//2
            if mid == 0:
                return 0
            if  checker(mid):
                l = mid +1
            else:
                h = mid - 1


        return h