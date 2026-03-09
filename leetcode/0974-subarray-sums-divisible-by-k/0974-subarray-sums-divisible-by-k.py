class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = 0
        seen = defaultdict(int)
        seen[0] += 1
        ans = 0

        for num in nums:
            pre += num
            if pre % k in seen:
                ans += seen[pre % k]
            seen[pre % k] += 1

        return ans