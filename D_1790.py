import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = number()
    arr1 = listed()
    arr2 = listed()

    ans = []

    def sorting(arr,num):
        swapped = True
 
        while swapped:
            swapped = False
            for k in range(1,n):
                if arr[k] < arr[k-1]:
                    ans.append([num,k])
                    arr[k],arr[k-1] = arr[k-1],arr[k]
                    swapped = True
        return arr
    
    arr1 = sorting(arr1,1)
    arr2 = sorting(arr2,2)

    
    for i in range(n):
        if arr1[i] > arr2[i]:
            arr1[i],arr2[i] = arr2[i],arr1[i]
            ans.append([3,i+1])

    arr1 = sorting(arr1,1)
    arr2 = sorting(arr2,2)

    print(len(ans))
    [print(a,b) for a,b in ans if len(ans)> 0]





    
test_cases = number()
for _ in range(test_cases):
    solve()
