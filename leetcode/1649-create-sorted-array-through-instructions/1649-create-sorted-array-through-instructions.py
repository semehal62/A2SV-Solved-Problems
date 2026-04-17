class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = []
        cost = 0
        mod = 10 ** 9 + 7 
        for ins in instructions:
            index1 = bisect_left(arr,ins)
            index2 = bisect_right(arr,ins)

            left = index1
            right = len(arr) - index2

            cost += min(left,right)
            bisect.insort(arr,ins)

        return cost % mod



