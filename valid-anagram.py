class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 =  Counter(s)
        dic2 = Counter(t)

        if dic1 == dic2:
            return True
        else:
            return False
