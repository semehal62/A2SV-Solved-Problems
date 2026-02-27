class Solution:
    def atmost(self,arr,k):
        count = defaultdict(int)
        left = 0 
        sub = 0
        for right in range(len(arr)):
            count[arr[right]] += 1
            while len(count) > k:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    del count[arr[left]]
                left += 1
            sub += right - left + 1

        return sub


    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k) -  self.atmost(nums,(k-1))
