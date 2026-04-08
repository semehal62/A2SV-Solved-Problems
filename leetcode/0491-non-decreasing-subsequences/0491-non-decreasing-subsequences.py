class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        def recur(idx):
            if len(curr) >= 2:
                res.add(tuple(curr))
            if idx == len(nums):
                return
            if not curr or curr[-1] <= nums[idx]:
                curr.append(nums[idx])
                recur(idx+1)
                curr.pop()
            recur(idx+1)

        recur(0)


        return list(res)


                