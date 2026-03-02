import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n, k = listed()
    arr = listed()

    count = defaultdict(int)

    left = 0
    longest = 0
    ans = []
    for right in range(n):
        count[arr[right]] += 1
        while len(count) > k:
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left += 1

        if longest < right- left+ 1:
            longest = right - left + 1
            ans = [left+1,right+1]

            
    print(*ans)

test_cases = 1
for _ in range(test_cases):
    solve()
