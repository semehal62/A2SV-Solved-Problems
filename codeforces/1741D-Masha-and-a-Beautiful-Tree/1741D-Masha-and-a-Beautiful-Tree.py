import math
import bisect
import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = number()
    arr = listed()
    
    count = 0
    def merge(left,right):
        nonlocal count 
        l,r = len(left) - 1,0

        if left[l] > right[r]:
            count += 1
            left,right = right,left
        
        return left + right

    def mergesort(l,r):
        if l == r:
            return [arr[l]]
        
        mid = (l+r)//2
        left = mergesort(l,mid)
        right = mergesort(mid+1,r)
        
        return merge(left,right)

    arr = mergesort(0,n-1)
    if arr == sorted(arr):
        print(count)
    else:
        print(-1)

test_cases = number()
for _ in range(test_cases):
    solve()