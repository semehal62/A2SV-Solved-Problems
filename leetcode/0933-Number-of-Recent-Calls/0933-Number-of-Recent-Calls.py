class RecentCounter:

    def __init__(self):
        self.stack = deque()
    

    def ping(self, t: int) -> int:
        self.stack.append(t)
        for i in range(len(self.stack)):
            if t-3000 <= self.stack[0] <= t:
                return len(self.stack)
            while self.stack and  self.stack[0] < t- 3000:
                self.stack.popleft()
            

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)