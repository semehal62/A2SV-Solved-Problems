import math
import bisect
import sys

from collections import defaultdict, Counter, deque
input = sys.stdin.readline

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: print("YES") if condition else print("NO")

def solve():
    n,m = listed()
    edges = []

    parent = [i for i in range(n+1)]
    size = [1] * (n+1)

    for i in range(m):
        u,v,w = listed()
        edges.append((w,u,v))

    edges.sort()

    def find(x):
        while x != parent[x]:
            x = parent[x]
            parent[x] = parent[parent[x]]

        return x


    def union(x,y):
        root1 = find(x)
        root2 = find(y)

        if root1 != root2:
            if size[root1] < size[root2]:
                root1,root2 = root2,root1

            parent[root2] = root1
            size[root1] += size[root2]
            return True
        else:
            return False

    ans = 0
    for w,u,v in edges:
        if union(u,v):
            ans += w

    print(ans)


test_cases = 1
for _ in range(test_cases):
    solve()