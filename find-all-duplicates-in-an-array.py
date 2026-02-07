class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        arr = []
        for key,value in count.items():
            if value == 2:
                arr.append(key)

        return arr        
