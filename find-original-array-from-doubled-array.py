class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()  
        dict1 = Counter(changed)
        arr = []
        for i in range(len(changed)):
            if  dict1[changed[i]] > 0 :
                if changed[i] == 0:
                    if dict1[changed[i]] > 1: 
                        arr.append(changed[i])
                        dict1[changed[i]] -= 2
                else:
                    sqr = changed[i] * 2
                    if dict1[sqr] > 0: 
                        arr.append(changed[i])
                        dict1[sqr] -= 1
                        dict1[changed[i]] -= 1

        return arr  if len(arr) ==(len(changed) // 2) else []
