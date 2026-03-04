class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            prefix.append(sums)

        
        subs = 0
        seen = defaultdict(int)

        for j in range(len(prefix)):
            if prefix[j] == k:
                subs += 1
            if (prefix[j]-k) in seen:
                subs += seen[(prefix[j]-k)]

            seen[prefix[j]] += 1
        

            

        return subs