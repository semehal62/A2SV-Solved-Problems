class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        arr = sorted(count_nums.items() ,key= lambda x:(-x[1],x[0]))

        maxi = arr[0][0]
        freq = count_nums[maxi]

        count_left , count_right = 0, 0
        for i in range(len(nums)):
            if nums[i] == maxi:
                count_left += 1
                count_right = freq - count_left
                print(count_left,count_right,maxi)
            if count_left > ((i + 1)//2) and count_right > ((len(nums) - i - 1)//2):
                return i

        return -1





        
