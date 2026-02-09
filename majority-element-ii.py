class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = n/3
        count = Counter(nums)
        arr = []
        for key, val in count.items():
            if val > k:
                arr.append(key)

        return arr
