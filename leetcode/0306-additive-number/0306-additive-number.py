class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        arr = []
        def backtracking(idx):
            if idx == len(num):
                if len(arr) >= 3:
                    if (arr[0][0] == "0" and arr[0] != "0") or (arr[1][0] == "0" and arr[1] != "0"):
                        return False
                    for j in range(2, len(arr)):
                        if int(arr[j-1]) + int(arr[j-2]) != int(arr[j]) or (arr[j] != "0" and arr[j][0] == "0"):
                            return False
                    return True
                return False
                
            
            for i in range(idx,len(num)):
                val = num[idx:i+1]
                if len(arr) >= 2 and int(arr[-1]) + int(arr[-2]) != int(val):
                    continue
                arr.append(val)
                if backtracking(i+1):
                    return True
                arr.pop()

            return False

        return backtracking(0)
                