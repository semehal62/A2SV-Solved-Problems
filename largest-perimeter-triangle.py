class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        right = 2
        left = 0
        parameter = 0
        sums = 0
        while right < len(nums):
            sums = sum(nums[left:right+1])
            if (sums - nums[left]) > nums[left] and  (sums - nums[left+1]) > nums[left+1]and (sums - nums[left+2]) > nums[left+2]:
                parameter = max(parameter ,sums)
            right += 1
            left += 1
