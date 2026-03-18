class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        def length(n,num):
            if n == 0:
                return 1

            if n == 1:
                return num
            
            elif (n & 1):
                val = length(n//2,num) % mod
                return num * val * val 

            else:
                val = length(n//2,num) % mod 
                return val * val 


                

        return ((length((n+1)//2 ,5))  * (length(n//2,4))) % mod 
            