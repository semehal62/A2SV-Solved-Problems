class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = nums[::]
        if len(nums) == 1:
            return nums[0]
        
        all_neg = True if nums[0] < 0 else False
        for i in range(1,len(nums)):
            if  nums[i] > 0:
                all_neg = False 
            nums[i] += nums[i - 1]
            
        if all_neg:
            return max(arr)

        mini = 0
        res = 0

        for j in range(len(nums)):
            mini = min(mini,nums[j])
            res = max(res, abs(nums[j] - mini))
            print(mini,nums[j])
            

        return res


        