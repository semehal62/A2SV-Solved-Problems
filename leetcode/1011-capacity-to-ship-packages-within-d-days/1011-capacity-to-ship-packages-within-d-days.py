class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(capacity):
            count = 1
            sums = 0
            for i in range(len(weights)):
                if sums + weights[i] > capacity:
                    sums = weights[i]
                    count += 1
                else:
                    sums += weights[i]
                            
            return count <= days
               


        low = max(weights)
        high = sum(weights)
        res = high
        while low <= high:
            mid = (low + high) // 2
            if checker(mid):
                res = min(res,mid)
                high = mid-1
            else:
                low = mid+1



        return res