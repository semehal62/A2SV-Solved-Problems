class RandomizedSet:

    def __init__(self):
        self.seen = set()
        self.ins = list()

    def insert(self, val: int) -> bool:
        if val not in self.seen:
            self.seen.add(val)
            self.ins.append(val)
            return True
        else:
            return False
      

    def remove(self, val: int) -> bool:
        if val  in self.seen:
            self.ins.remove(val)
            self.seen.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        x = random.choice(self.ins)
        return x


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
