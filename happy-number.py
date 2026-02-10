class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visted = set()
        while n not in visted:
            visted.add(n)
            temp = 0
            while n != 0:
                temp += (n % 10 ) ** 2
                n //= 10

            n = temp 
            if n == 1:
                return True
            if n == 2:
                return False
        return False
        
