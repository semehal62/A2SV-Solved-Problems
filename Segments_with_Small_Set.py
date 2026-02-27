import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n,k = listed()
    arr = listed()

    left = 0
    seen = defaultdict(int)
    count = 0
    for right in range(len(arr)):
        seen[arr[right]] += 1
    
        while len(seen) > k:
            seen[arr[left]] -= 1
            if seen[arr[left]] == 0:
                del seen[arr[left]]
            left += 1
        
 
        count += right-left + 1
            

    print(count)



test_cases = 1
for _ in range(test_cases):
    solve()
