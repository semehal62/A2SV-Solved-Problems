class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = copy.deepcopy(nums)
        # nums = list(set(nums))
        nums.sort()

        
        indexs = defaultdict(int)
        seen = set()
        for i in range(len(nums)):
            if i == 0 :
                indexs[nums[i]] = i
            if nums[i] not in seen:
                indexs[nums[i]] = i
                seen.add(nums[i])
  

        ans = []
        for j in range(len(temp)):
            ans.append(indexs[temp[j]])

        return ans
