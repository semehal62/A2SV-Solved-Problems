class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        result = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               result[j][n-i] =   matrix[i][j] 

        for k in range(len(matrix)):
            for l in range(len(matrix[0])):
                 matrix[k][l] = result[k][l]
                

        
