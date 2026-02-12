class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        colunm = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    colunm.add(j)

        for k in range(len(matrix)):
            for w in range(len(matrix[0])):  
                if k in row or w in colunm:
                    matrix[k][w] = 0
