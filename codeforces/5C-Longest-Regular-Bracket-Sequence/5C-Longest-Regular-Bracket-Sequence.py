import sys
from collections import defaultdict, Counter, deque

number = lambda: int(input())
listed = lambda: list(map(int, input().strip().split()))
yn = lambda condition: "YES" if condition else "NO"

def solve():
    s = input()
    stack = []
    
    for i in range(len(s)):
        if s[i] == ")":
            num = 0
            while stack and stack[-1].isdigit():
                num += int(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
                num += 2
                stack.append(str(num))
            else:
                stack.append(str(num))
                stack.append(s[i])
                
        else:
            stack.append(s[i])


    stk = 0
    mx = [-1, 1]
    # print(stack)
    for cur in stack:
        if not cur.isdigit():
            if mx[0] < stk:
                mx = [stk, 1]
            elif mx[0] == stk:
                mx[1] += 1
            stk = 0
        else:
            stk += int(cur)
    if mx[0] < stk:
        mx = [stk, 1]
    elif mx[0] == stk:
        mx[1] += 1
    if mx[0] == 0:
        print(0, 1)
    else:
        print(*mx)

    # for i in range(len(stack)):
    #     if stack2 and stack2[-1].isdigit() and stack[i].isdigit():
    #         stack2[-1] = str(int(stack2[-1]) + int(stack[i]))
    # if max(stack).isdigit() and max(stack) != "0":
    #     print(max(stack), stack.count(max(stack)))
    #     return

    # print(0, 1)
    
    
    





test_cases = 1
for _ in range(test_cases):
    solve()