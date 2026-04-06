class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # binary search

        n = len(citations)
        low = 1
        high = n
        ans = 0 
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if citations[n - mid] >= mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1 
        return ans