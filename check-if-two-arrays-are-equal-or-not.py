class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        from collections import Counter
        if len(a) != len(b):
            return False
        else:
            dict1 = Counter(a)
            dict2 = Counter(b)
            
            for key,value in dict1.items():
                if key not in dict2 or value != dict2[key]:
                    return False
            return True
                    
