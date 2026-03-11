class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            res = 0
            if s[i] == ")":  
                while stack[-1] != "(":
                    res += stack.pop() * 2
                res += 1 if res == 0 else 0
                stack.pop()
                stack.append(res)
            else:
                stack.append(s[i])

        return sum(stack)