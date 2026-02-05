class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        arr = []
        for i in range(left,right + 1):
            arr.append(i)
        

        for j in arr:
            is_in = False
            for time in ranges:
                if j == time[0] or  j == time[1]:
                    is_in = True
                    break
                elif j > time[0]   and j < time[1]:
                    is_in = True
                    break
            if is_in == False:
                return False
        return True
            
