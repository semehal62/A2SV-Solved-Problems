import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n = number()
    b = input()
    a = input()

    b  = list(b)
    c = b[::]
    prefix = []


    sums = 0
    for i in range(len(b)):
        sums += int(b[i])
        prefix.append(sums)

    i = 0
    for j in range(len(b)-1,-1,-1):
        if j % 2 != 0:
            if prefix[j] != n- prefix[j] and int(a[j]) != ((int(c[j])+i) % 2):
                print("NO")
                return 

            if int(a[j]) != ((int(c[j])+i) % 2):
                i = 1- i 

        else:
            if int(a[j]) != ((int(c[j])+i) % 2):
                print("NO")
                return
        n -= 1

    print("YES")     



test_cases = number()
for _ in range(test_cases):
    solve()