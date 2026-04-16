class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            pos = nums[i] - 1
            if pos != i and nums[pos] != nums[i]:
                nums[i],nums[pos] = nums[pos],nums[i]
            elif pos != i and nums[pos] == nums[i]:
                return nums[i]
            else:
                i += 1

