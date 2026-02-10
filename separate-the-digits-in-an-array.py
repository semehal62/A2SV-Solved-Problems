class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            num = str(num)
            for i in num:
                arr.append(int(i))

        return arr
