class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = [0]*(len(citations) + 1)
       
        for i in range(len(citations)):
            if citations[i] > len(citations):
                papers[-1] += 1
            else:
                papers[citations[i]]  += 1


        sums = 0
        for j in range(len(papers)-1,-1,-1):
            sums += papers[j]
            if sums >=  j and j != 0:
                return j 
            elif j == 0 and sums > 0:
                return 0
 
