class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        seen = defaultdict(int)
        count = 0
        for j in range(len(nums)):
            if nums[j] - goal == 0:
                count += seen[0] +1 if seen[0] > 0 else 1
            elif (nums[j] - goal) in seen:
                count += seen[nums[j]-goal]
                
            seen[nums[j]] += 1


        return count

