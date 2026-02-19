class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        index =  len(piles) -2
        ans = 0
        left = 0
        
        while index > left:
            ans += piles[index]
            index -= 2
            left += 1
            
        return ans 
