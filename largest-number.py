class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        def custom(a, b):
            one = a + b
            two = b + a
            if one < two:
                return 1
            return -1
        nums.sort(key=cmp_to_key(custom))
        ans = "".join(nums)
        return "0" if ans[0] == "0" else ans
