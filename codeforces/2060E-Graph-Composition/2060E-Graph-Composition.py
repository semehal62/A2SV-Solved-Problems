import math
import bisect
import sys

from collections import defaultdict, Counter, deque
input = sys.stdin.readline

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: print("YES") if condition else print("NO")


def solve():

    n,m1,m2 = listed()
    parf = [i for i in range(n +1)]
    parg = [i for i in range(n+1)]
    sizef = [1] * (n +1)
    sizeg = [1] * (n +1)

    def find(x,par):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]

        return x

    def union(u,v,par,size):
        root1 = find(u,par)
        root2 = find(v,par)

        if root1 != root2:
            if size[root1] < size[root2]:
                root1, root2 = root2, root1
            
            par[root2] = root1
            size[root1] += size[root2] 
    def check1(u, v):
        return find(u, parg) == find(v, parg)

    
    f = [listed() for _ in range(m1)]

    for i in range(m2):
        u,v = listed()
        union(u,v,parg,sizeg)
    ans = 0
    for u, v in f:
        if check1(u, v):
            union(u,v,parf,sizef)
        else:
            ans += 1
    group = [[] for i in range(n+1)]

    for i in range(1,n+1):
        part = find(i, parg)
        group[part].append(i)

    for g in group:
        for j in range(1,len(g)):
            u, v = g[0], g[j]
            if find(u,parf) != find(v,parf):
                ans += 1
                union(u,v,parf,sizef)

    print(ans)

    

    



test_cases = number()
for _ in range(test_cases):
    solve()