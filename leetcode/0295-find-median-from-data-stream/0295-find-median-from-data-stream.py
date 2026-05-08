class MedianFinder:

    def __init__(self):
        self.mini = []
        self.maxi = []

    def addNum(self, num: int) -> None:
        if len(self.mini) == len(self.maxi):
            heappush(self.maxi,-num)
        else:
            heappush(self.mini,num)
            
        if self.maxi and self.mini:
            mn_max =- heappop(self.maxi)
            mx_mini = heappop(self.mini)
            if mn_max < mx_mini:
                heappush(self.mini,mx_mini)
                heappush(self.maxi,-mn_max)
            else:
                heappush(self.mini,mn_max)
                heappush(self.maxi,-mx_mini)


    def findMedian(self) -> float:
        if len(self.mini) == len(self.maxi):
            mn = heappop(self.mini)
            mx = - heappop(self.maxi)
            heappush(self.mini,mn)
            heappush(self.maxi,-mx)

            return (mn + mx) / 2
        else:
            res = - heappop(self.maxi)
            heappush(self.maxi,-res)
            return res        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()