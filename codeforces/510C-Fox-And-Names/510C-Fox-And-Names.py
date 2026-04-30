import math
import bisect
import sys

from collections import defaultdict, Counter, deque
# input = sys.stdin.readline().strip

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: print("YES") if condition else print("NO")

def solve():
    n = number()
    word = [input() for _ in range(n)]

    adj_list = [[] for _ in range(26)]
    depend = [0] * 26

    for i in range(1,n):
        prev = word[i-1]
        curr = word[i]
        # print(prev, curr)
        for i in range(len(curr)):
            if i == len(prev): break
            if prev[i] != curr[i]:
                asci = ord(curr[i]) % 97
                adj_list[ord(prev[i]) % 97].append(asci)
                depend[asci] += 1
                break
        else:
            if len(curr) < len(prev):
                print("Impossible")
                return
    # print(adj_list)
    
    alpha = ""
    q = deque()
    
    for i in range(26):
        if depend[i] == 0:
            q.append(i)
   
    while q:
        node = q.popleft()
        alpha += chr(node + 97)
        
        for child in adj_list[node]:
            depend[child] -= 1
            if depend[child] == 0:
                q.append(child)
    if len(alpha) != 26:
        print("Impossible")
        return
    print(alpha)


test_cases = 1
for _ in range(test_cases):
    solve()