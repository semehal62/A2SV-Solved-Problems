class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        for i in range(len(nums1)):
            arr.append(nums1[i]-nums2[i])

        nums = []
        count = 0
        for i in range(len(arr)):
            idx = bisect_left(nums,arr[i]+diff+1)
            count += idx
            bisect.insort(nums,arr[i])

        return count

        


