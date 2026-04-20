import math
import bisect
import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    sent = input()
    recived = input()
    res = []
    def recur(idx,sums):
        if idx == len(recived):
            res.append(sums)
            return
        
        if recived[idx] == "+":
            recur(idx + 1, sums+1)
        elif recived[idx] == "-":
            recur(idx + 1, sums-1)
        else:
            recur(idx + 1,sums+1)
            recur(idx + 1,sums-1)

    recur(0,0)

    target = 0
    for i in range(len(sent)):
        if sent[i] == "+":
            target += 1
        else:
            target -= 1

    count = 0
    total = len(res)

    for i in range(total):
        count += 1 if res[i] == target else 0

    print(count/total)



test_cases = 1
for _ in range(test_cases):
    solve()