class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums)+1)
        surfix = [1] * (len(nums)+1)

        pro = 1
        for i in range(len(nums)):
            pro *= nums[i]
            prefix[i+1] = pro

        pro = 1
        for i in range(len(nums)-1,-1,-1):
            pro *= nums[i]
            surfix[i] = pro


        ans = []

        print(prefix,surfix)
        for j in range(1,len(prefix)):
            res = prefix[j-1] * surfix[j]
            ans.append(res)
            res = 1
       

        return  ans



        