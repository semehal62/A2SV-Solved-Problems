class Solution:
    def findMin(self, nums: List[int]) -> int:
        def merge(l,r):
            if l == r:
                return [nums[l]]

            mid = (l+r)//2
            left = merge(l,mid)
            right = merge(mid+1,r)

            return sorted(left+right)

        return merge(0,len(nums)-1)[0]

