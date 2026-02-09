class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)
        self.values = defaultdict(int)

    def add(self, number: int) -> None:
        if self.count[number] in self.values:
            self.values[self.count[number]] -= 1
        self.count[number] += 1
        self.values[self.count[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.count[number] >  0:
            self.values[self.count[number]] -= 1
            self.count[number] -= 1
            self.values[self.count[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.values[frequency] > 0:
            return True
        else:
            return False
