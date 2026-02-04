class Solution(object):
    def longestCommonPrefix(self, strs):
        first= strs[0]
        for i in range(1,len(strs)):
            second=strs[i]
            j=0
            k=0
            while(j<len(first) and k<len(second)):
                if first[j]==second[k]:
                    j+=1
                    k+=1
                    
                else:
                    break
            first= first[0:j]
        return first
