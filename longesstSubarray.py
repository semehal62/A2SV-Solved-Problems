class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        longest = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[0] > 1:
                count[nums[left]] -= 1
                left += 1
        
            longest = max(longest,right-left)

        return longest
