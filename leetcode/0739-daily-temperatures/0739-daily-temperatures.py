class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        pair = defaultdict(int)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                x = stack.pop()
                pair[x] = abs(x-i)
            stack.append(i)

        arr = [pair[i] for i in range(len(temperatures))]
        
        

        return arr