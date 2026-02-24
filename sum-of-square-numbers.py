class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = ceil(sqrt(c))
        print(right)
        while left < right:
            if left**2 + right**2 == c:
                return True 
            elif left**2 + right**2  > c:
                right -= 1
            else:
                left += 1
      

    

                
        if c % 2 == 0:
            if sqrt(c//2) == int(sqrt(c//2)):
                return True

        return False
        
