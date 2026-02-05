#User function Template for python3
class Solution:
    #Function to check if a is a subset of b.
    from collections import Counter
    def isSubset(self, a, b):
        # Your code here
        count_a = self.Counter(a)
        count_b = self.Counter(b)
        
        for key,value in count_b.items():
            if key not in  count_a or value > count_a[key]:
                return False
        return True 
                
        
    
