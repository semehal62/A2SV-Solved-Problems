class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(len(matrix)):
            arr.extend(matrix[i])

        heapify(arr)
        

        k = len(arr) - k +1
        while len(arr) > k:
            heappop(arr)

        return arr[0]