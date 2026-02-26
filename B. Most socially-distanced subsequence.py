import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = number()
    arr = listed()

    arr = [0] + arr

    ans = []
    for i in range(1,n+1):
        if i == 1 or i == n or ((arr[i-1] < arr[i]) != (arr[i]< arr[i+1])):
            ans.append(arr[i])
   


        

    print(len(ans))
    print(" ".join(map(str,ans)))


test_cases = number()
for _ in range(test_cases):
    solve()
