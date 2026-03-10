class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.container = []
        

    def consec(self, num: int) -> bool:
        
        while self.container and self.container[-1] != num:
            self.container.pop()
            
        if num == self.value:
            self.container.append(num)
        
        return True if len(self.container) >= self.k else False
        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)