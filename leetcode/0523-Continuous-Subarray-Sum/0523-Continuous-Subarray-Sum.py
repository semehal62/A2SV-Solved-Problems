class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix = []
        prefix.append(nums[0])
        sums = nums[0]
        for i in range(1,len(nums)):
            sums += nums[i]
            if sums % k == 0:
                return True 

            prefix.append(sums)

        rem_mod = defaultdict(int)

        for i in range(len(prefix)):
            res = prefix[i] % k
            
            if res in rem_mod and abs(rem_mod[res] - i) >= 2:
                return True

            if res not in rem_mod:
                rem_mod[res] = i

        return False