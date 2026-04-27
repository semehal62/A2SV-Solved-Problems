class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3

        for i in range(len(nums)):
            arr[nums[i]] += 1

        j = 0
        print(arr)
        for i in range(len(arr)):
            temp = arr[i]
            while temp > 0:
                nums[j] = (i)
                j += 1
                temp -= 1
        


                

        