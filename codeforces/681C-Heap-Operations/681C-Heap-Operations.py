import math
import bisect
import sys
import heapq

from collections import defaultdict, Counter, deque
input = sys.stdin.readline

number = lambda: int(input())
listed = lambda: list(map(str, input().strip().split()))
yn = lambda condition: print("YES") if condition else print("NO")

def solve():
    n = number()

    instraction = []

    for i in range(n):
        inst = listed()
        instraction.append(inst)

    ans = []
    arr = []
    for inst in instraction:
        if inst[0] == "insert":
            ans.append(" ".join(inst))
            heapq.heappush(arr,int(inst[1]))

        elif inst[0] == "getMin":
            mini = int(inst[1])
            if arr:
                val = heapq.heappop(arr)
                while val < mini:
                    ans.append("removeMin")
                    if arr:
                        val = heapq.heappop(arr)
                    else:
                        break

                if val > mini:
                    heapq.heappush(arr,val)
                    heapq.heappush(arr,mini)
                    s = "insert " + str(mini)
                    ans.append(s)
                elif val == mini:
                    heapq.heappush(arr,val)
                else:
                    heapq.heappush(arr,mini)
                    s = "insert " + str(mini)
                    ans.append(s)
                    
                
            else:
                heapq.heappush(arr,mini)
                s = "insert " + str(mini)
                ans.append(s)
                
            ans.append(" ".join(inst))
        elif inst[0] == "removeMin":
            if arr:
                heapq.heappop(arr)
            else:
                ans.append("insert 1")

            ans.append(" ".join(inst))
      
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])
        






test_cases = 1
for _ in range(test_cases):
    solve()