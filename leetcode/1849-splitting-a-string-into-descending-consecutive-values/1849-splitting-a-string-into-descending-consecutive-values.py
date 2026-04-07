class Solution:
    def splitString(self, s: str) -> bool:
        arr = []
        def into(idx):
            nonlocal arr
            if idx == len(s):
                for i in range(1,len(arr)):
                    if int(arr[i-1]) - int(arr[i]) != 1:
                        return False

                return len(arr) >= 2

            
            
            
            for i in range(idx,len(s)):
                val = s[idx:i+1]
                if arr and int(arr[-1]) - int(val) != 1:
                    continue
                arr.append(val)
                if into(i+1):
                    return True
                arr.pop()
                
            return False
            


        return into(0)