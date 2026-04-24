import sys
import bisect
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n,m = listed()
    a = listed()
    b = sorted(listed())

    if n == 1:
        print("YES")
        return


    INF = [float("-inf")]
    a = INF + a
    for i in range(1,n+1):
        idx = bisect.bisect_left(b,a[i]+a[i-1])
        if idx == m:
            if a[i] < a[i-1]:
                print(yn(0))
                return
            else:
                continue
        
        if a[i-1] <= a[i] and a[i-1] <= (b[idx]-a[i]):
            a[i] = min(a[i],b[idx]-a[i])
        elif a[i-1] <= b[idx]-a[i]:
            a[i] = b[idx]-a[i]
        else:
            print(yn(0))
            return

        
    
    print(yn(sorted(a) == a))

test_cases = number()
for _ in range(test_cases):
    solve()