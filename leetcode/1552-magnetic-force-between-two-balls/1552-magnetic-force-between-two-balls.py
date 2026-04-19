class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def checker(diff):
            beg = 0
            count = 0
            for i in range(1,len(position)):
                if abs(position[i] -position[beg]) >= diff:
                    count += 1
                    beg = i
            count += 1
            return count >= m 
            
                    

        right = position[-1] - position[0]
        left = 1
           
        while left <= right:
            mid = (left + right)// 2
            if checker(mid):
                left = mid + 1
            else:
                right = mid -1
           
        return right