class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        maxi = float('inf')
        arr = [0] * k
        child = k
        def recur(arr,i):
            nonlocal maxi,child
            if i == len(cookies):
                mx = max(arr)
                if maxi > mx:
                    maxi = mx
                return

            for j in range(k):
                # if arr[j] + cookies[i] < maxi:
                arr[j] += cookies[i]
                recur(arr,i+1)
                arr[j] -= cookies[i]

        recur(arr,0)
        return maxi

