class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # binary search

        n = len(citations)
        low = 0
        high = n
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            idx = bisect_left(citations, mid)
            if n - idx >= mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1 


        return ans
