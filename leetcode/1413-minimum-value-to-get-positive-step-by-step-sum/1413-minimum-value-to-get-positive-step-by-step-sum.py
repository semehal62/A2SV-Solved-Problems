class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i -1]

        mini = min(nums)
        mini = 1+ abs(mini) if mini < 0 else 1
        return mini

        