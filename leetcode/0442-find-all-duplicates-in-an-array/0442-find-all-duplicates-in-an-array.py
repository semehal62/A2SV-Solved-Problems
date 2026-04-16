class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        i = 0
        arr = []
        while i < n:
            postion = nums[i] - 1
            if postion in seen:
                arr.append(nums[i])
            else:
                seen.add(postion)
            i += 1

        return arr
        