import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def match(cleft,cright):
    ans = defaultdict(int)
    for key,value in cleft.items():
        if key in cright:
            x = min(value,cright[key])
            if x == value == cright[key]:
                cleft[key] = 0
                del cright[key]
            elif value == x:
                cleft[key]  = 0
                cright[key] -= x
            else:
                del cright[key] 
                cleft[key] -= x

    for key, val in cleft.items():
        if val != 0:
            ans[key] = val

    return ans,cright

def solve():
    n,l,r = listed()
    arr = listed()
    left, right = arr[:l], arr[l:]

    if l < r:
        left, right = right, left
        l, r = r, l

    cleft = Counter(left)
    cright = Counter(right)
    cleft,cright = match(cleft,cright)
    val_l = sum(cleft.values())
    val_r = sum(cright.values())

    req = (l - r) // 2
    operations = req

    if req != 0:
        for k,v in cleft.items():
            
            if v >= 2 :
                if v//2 > req:
                    cleft[k] -= req
                    cright[k] = req
                    break

                cleft[k] -= v//2
                cright[k] = v//2
                req -= v//2

        cleft,cright = match(cleft,cright)


    val_l = sum(cleft.values())
    val_r = sum(cright.values())

    operations += ((val_l + val_r) // 2)
    
    print(operations)            


test_cases = number()
for _ in range(test_cases):
    solve()
