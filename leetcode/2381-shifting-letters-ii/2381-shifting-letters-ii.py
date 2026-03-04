class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]* (len(s)+1)

        for a,b,c in shifts:
            if c:
                arr[a] += 1
                arr[b+1] -= 1
            else:
                arr[a] -= 1
                arr[b+1] += 1


        for i in range(1,len(arr)):
            arr[i] += arr[i-1]


        s = list(s)
        for j in range(len(s)):
            s[j] = chr(97 +  (((ord(s[j]) + arr[j])-97)%26)) 

        return "".join(s)

