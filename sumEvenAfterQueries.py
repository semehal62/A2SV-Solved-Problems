class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sums = sum(num for num in nums if num % 2 == 0)
        for vali,indexi in queries:
            if nums[indexi] % 2 == 0:
                sums -= nums[indexi]
            nums[indexi] = nums[indexi] + vali
            if nums[indexi] % 2 == 0:
                sums += nums[indexi]
            ans.append(sums)
        
        return  ans
