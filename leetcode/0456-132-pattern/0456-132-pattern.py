class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
       
        stack = []
        mini = float("inf")
        for i in range(len(nums)):
            mini = min(mini,nums[i])
            while stack and stack[-1][0] < nums[i]:
                stack.pop()

            if  stack and stack[-1][0] > nums[i] > stack[-1][1]:
                return True
            stack.append((nums[i],mini))

        return False
            



        




        