class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        def recur(idx):
            if len(curr) >= 2 and tuple(curr) not in res:
                res.add(tuple(curr))
            if idx == len(nums):
                return

            for i in range(idx,len(nums)):
                if curr and curr[-1] >  nums[i]:
                    continue
                curr.append(nums[i])
                recur(i+1)
                curr.pop()
                recur(i+1)


        recur(0)


        return list(res)


                