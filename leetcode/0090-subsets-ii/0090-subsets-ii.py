class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def recur(idx,arr):
            if idx == len(nums):
                return 
            
            arr.append(nums[idx])
            res.add(tuple(sorted(arr)))
            recur(idx+1,arr)

            arr.pop()
            res.add(tuple(sorted(arr)))
            recur(idx+1,arr)

        recur(0,[])

        res = list(res)
        



        return res