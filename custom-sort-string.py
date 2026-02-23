class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0]*26 



        for i in range(len(s)):
            count[ord(s[i])%97] += 1

            
        ans = ""
        for j in range(len(order)):
            if count[ord(order[j])%97] > 0:
                ans += order[j] * count[ord(order[j])%97]
                count[ord(order[j])%97] = 0
        
        for k in range(len(count)):
            if count[k] > 0:
                ans += chr(k+97)* count[k]
                

        return ans
