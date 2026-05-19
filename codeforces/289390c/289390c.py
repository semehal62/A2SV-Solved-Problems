import math
import bisect
import sys

from collections import defaultdict, Counter, deque
input = sys.stdin.readline

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
strs = lambda: list(map(str, input().strip().split()))
yn = lambda condition: print("YES") if condition else print("NO")

def solve():
    n,m = listed()
    parent = [i for i in range(n+1)]
    size = [1] * (n+1)
    exp = [0] * (n+1)
    def find(x):
        while x != parent[x]:
            x = parent[x]
        
        return x
    
    def find_exp(x):
        ans = 0
        while x != parent[x]:
            ans += exp[x]
            x = parent[x]

        return ans + exp[x]
    
    def join(x,y):
        root1 = find(x)
        root2 = find(y)

        if root1 != root2:
            if size[root1] < size[root2]:
                root1, root2 = root2,root1

            parent[root2] = root1
            exp[root2] -= exp[root1]
            size[root1] += size[root2]

    for i in range(m):
        command = strs()
        if command[0] == "join":
            join(int(command[1]),int(command[2]))
        elif command[0] == "add":
            val = find(int(command[1]))
            exp[val] += int(command[2])
        else:
            res = find_exp(int(command[1]))
            print(res)


test_cases = 1
for _ in range(test_cases):
    solve()