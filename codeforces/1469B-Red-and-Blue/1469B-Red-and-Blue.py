import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = number()
    red = listed()
    m = number()
    blue = listed()


    for i in range(1,len(red)):
        red[i] += red[i-1]

    for i in range(1,len(blue)):
        blue[i] += blue[i-1]


    upper = max(red)
    lower = max(blue)
    
    if upper >= 0 and lower >= 0:
        ans = upper + lower
    elif upper > 0 and lower < 0:
        ans = upper
    elif upper < 0 and lower > 0:
        ans = lower
    else:
        ans = 0
    
    print(max(ans,0))


test_cases = number()
for _ in range(test_cases):
    solve()