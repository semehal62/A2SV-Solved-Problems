class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pos(x,n):
            if n == 1:
                return x
            elif (n & 1):
                val =  pos(x,n//2)
                return x * val * val
            else:
                val =  pos(x,n//2)
                return val * val
            

        if  x == 0:
            return x
        elif n == 0:
            return 1.00000
        elif n > 0:
            return pos(x,n) 
        else:
            n = -1 * n
            val = pos(x,n)
            return 1/val

        