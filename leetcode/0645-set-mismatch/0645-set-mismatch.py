class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        i = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] in seen:
                ans.append(nums[i])
            seen.add(nums[i])

        for j in range(len(nums)):
            if j+1 not in seen:
                ans.append(j+1)
                return ans