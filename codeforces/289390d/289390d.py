import math
import bisect
import sys

from collections import defaultdict, Counter, deque
input = sys.stdin.readline

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
stred = lambda: list(map(str, input().strip().split()))
yn = lambda condition: print("YES") if condition else print("NO")

def solve():
    n,m,k = listed()
    parent = [i for i in range(n+1)]
    size = [1] * (n+1)

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

    edges = []

    for i in range(m):
        edges.append((listed()))


    queries = []
    for i in range(k):
        que = stred()
        queries.append(que)

    queries = queries[::-1]

    ans = []

    for com,x,y in queries:
        if com == "ask":
            val = find(int(x)) == find(int(y))
            ans.append(val)
        else:
            union(int(x),int(y))


    ans = ans[::-1]

    for res in ans:
        yn(res)

test_cases = 1
for _ in range(test_cases):
    solve()