class node:
    def __init__(self,val):
        self.prev = None
        self.next = None
        self.val = val

class BrowserHistory(node):

    def __init__(self, homepage: str):
        self.home = node(homepage)
        self.head = self.home
        self.curr = self.head
        


    def visit(self, url: str) -> None:
        site = node(url)
        site.prev = self.curr
        self.curr.next = site
        self.curr = self.curr.next

        

    def back(self, steps: int) -> str:
        position = 0
        while self.curr and self.curr.prev  and position < steps:
            self.curr = self.curr.prev
            position += 1

        return self.curr.val
        

    def forward(self, steps: int) -> str:
        position = 0
        while self.curr and self.curr.next  and position < steps:
            self.curr = self.curr.next
            position += 1

        return self.curr.val
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)