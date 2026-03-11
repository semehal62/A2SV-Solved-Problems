class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            # print(stack)
            string = ""
            digit = ""

            if s[i] == "]":
                count = 1
                # finding the string
                while stack and stack[-1] != "[":
                    string += stack.pop()[::-1]
                stack.pop()

                # finding the digit
                while stack and stack[-1].isdigit():
                    digit += stack.pop()


                # mezergat
                string = string[::-1]
                digit = digit[::-1]
    
                stack.append(string * int(digit))
            else:
                stack.append(s[i])

        return "".join(stack)