class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()

        left = 0
        maxi = 0
        for i in range(len(nums)):
            while increasing and nums[i] < increasing[-1]:
                increasing.pop()
            increasing.append(nums[i])

            while decreasing and nums[i] > decreasing[-1]:
                decreasing.pop()
            decreasing.append(nums[i])

        
            while abs(increasing[0]- decreasing[0]) > limit:
                if nums[left] == increasing[0]:
                    increasing.popleft()
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                left += 1

            maxi = max(maxi, i-left+1)

        return maxi



           
