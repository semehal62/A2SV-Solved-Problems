import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n,k,q = listed()

    recipes = []
    for i in range(n+q):
        res = listed()
        recipes.append(res)

    question = recipes[n:]
    recipes = recipes[:n]
    mx = 200005
    

    arr = [0] * mx

    for a,b in recipes:
        arr[a] += 1
        arr[b+1] -= 1
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    sums = 0

    for j in range(len(arr)):
        if arr[j] >= k:
            sums += 1
        arr[j] = sums

    ans = []
    for jj in range(len(question)):
        a,b = question[jj]
        ans.append(arr[b]-arr[a-1])

    for w in range(len(ans)):
        print(ans[w])
            

test_cases = 1
for _ in range(test_cases):
    solve()