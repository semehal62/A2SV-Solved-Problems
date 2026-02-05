class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total=sum(nums)
        nsum=(n*(n+1))//2
        return nsum-total
