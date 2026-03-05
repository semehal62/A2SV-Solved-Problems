class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        sums = 0
        for i in range(len(matrix)): 
            for j in range(len(matrix[i])):
                sums += matrix[i][j] 
                matrix[i][j] = sums + matrix[i-1][j] if i > 0 else sums
            sums = 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
      
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2]  - self.matrix[row2][col1-1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2] 
        else:
              return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1] 





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)