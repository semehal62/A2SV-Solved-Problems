class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = defaultdict(list)
        arr = []
        def recur(i):
            if i == len(nums):
                if arr not in res[1]:
                    res[1].append(arr.copy())
                return

            arr.append(nums[i])
            recur(i+1)
            arr.pop()
            recur(i+1)
            
        recur(0)
        return res[1]
       