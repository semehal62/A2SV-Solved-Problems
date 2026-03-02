import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n,k = listed()
    s = input()

    left = 0
    
    f_window = defaultdict(int)
    count = 0
    for i in range(k):
        f_window[s[i]] += 1

    count = f_window["W"]


    for right in range(k,n):
        f_window[s[right]] += 1
        f_window[s[left]] -= 1
        left += 1
        count = min(count,f_window["W"])

    print(count)
