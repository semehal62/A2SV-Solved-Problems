import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    n,m = listed()
    matrix = []
    for _ in range(n):
        row = input()
        matrix.append(row)
    q = number()
    ranges = []

    for i in range(q):
        ques = listed()
        ranges.append(ques)

    horizontal = []

    for i in range(n):
        row = [0]
        for j in range(1,m):
            if matrix[i][j-1] == "." and matrix[i][j] == ".":
                row.append((row[-1]+1))
            else:
                row.append(row[-1])

        horizontal.append(row)

    # horizontal.append([0]*(m+1))

    for i in range(1,n):
        for j in range(m):
            horizontal[i][j] += horizontal[i-1][j]

 
    vertical = [[0]*m]   

    for i in range(1,n):
        row = []
        for j in range(m):
            if matrix[i-1][j] == "." and matrix[i][j] == ".":
                row.append((vertical[i-1][j] + 1))
            else:
                row.append(vertical[i-1][j])

        vertical.append(row)

    for i in range(n):
        for j in range(1, m):
            vertical[i][j] += vertical[i][j -1]

    
    ans = 0   
    for r1,c1,r2,c2 in ranges:
        r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
        ans = 0
        if r1 == 0 and c1 == 0:
            ans += vertical[r2][c2] + horizontal[r2][c2]
        elif r1 == 0:
            ans +=  (vertical[r2][c2]-vertical[r2][c1 - 1]) + (horizontal[r2][c2]- horizontal[r2][c1])
        
        elif c1 == 0:
            ans +=  (vertical[r2][c2]-vertical[r1][c2]) + (horizontal[r2][c2]- horizontal[r1-1][c2])
        else:
            ans +=  ((vertical[r2][c2]-vertical[r1][c2]-vertical[r2][c1-1]) + vertical[r1][c1-1]) + ((horizontal[r2][c2]- horizontal[r1-1][c2]-horizontal[r2][c1]) + horizontal[r1-1][c1])

        print(ans)
    

    



test_cases = 1
for _ in range(test_cases):
    solve()