import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = number()
    arr = listed()

    arr.sort()
    maxi = arr[-1]
    count = 0

    k = len(arr) - 1
    j = k -1
    i = 0
    while k >= 2:
        if i < j and arr[i] + arr[j] + arr[k]  > max(maxi,2*arr[k]):
            count += j-i
            j -= 1
            
        elif i < j:
            i += 1

        if i == j:
            k -= 1
            j = k-1
            i = 0
    
    print(count)
test_cases = number()
for _ in range(test_cases):
    solve()