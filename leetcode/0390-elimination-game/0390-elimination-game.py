class Solution:
    def lastRemaining(self, n: int) -> int:
        start = 1
        add = 1
        i = 0
        while start < n:
            count = ceil(n / add)
            if not i:
                if count % 2:
                    n -= add
                start += add
            else:
                if count % 2:
                    start += add
                n -= add
            add *= 2
            i = 1 - i
        return n           