class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        u = str(x)
        j = len(u) -1

        for i in range(len(u)):
            if j == i:
                return True
                
            if u[i] == u[j]:
                j -= 1
            else:
                return False

        return True
