class Solution:
    def counting(self,s,k,letter):
        left = 0
        s = list(s)
        longest = 0
        for right in range(len(s)):
            if s[right] != letter and k > 0:
                k -=1
            elif s[right] != letter and k == 0:
                while s[left] == letter and left < right:
                    left += 1
                left += 1
            longest = max(longest,right-left+1)

            print(left,right)
        return longest
            
    def characterReplacement(self, s: str, k: int) -> int:
        letters = list(set(s))
        counts = 0
        for let in letters:
            counts = max(counts,self.counting(s,k,let))

        
        return counts
