class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first = 0
        second = 0

        while second < len(haystack):

            if needle[first] == haystack[second]:
                first += 1
            elif first > 0:
                second -= first 
                first = 0
                
               
            second += 1

            if first == len(needle):
                return second - first

        


       

        return -1
