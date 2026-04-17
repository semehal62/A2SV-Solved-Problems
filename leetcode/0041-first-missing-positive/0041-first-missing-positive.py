class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        i = 0
        while i < len(nums):
            postion = abs(nums[i]) - 1
            if 0 <= postion < len(nums) and nums[postion] >= 0:
                if nums[postion] == 0:
                    nums[postion] = (len(nums) * -1)
                else:
                    nums[postion] *= -1
            i += 1

        i = 0
        while i < len(nums):
            if nums[i] >= 0:
                return i + 1
            else:
                i += 1

        return i + 1


