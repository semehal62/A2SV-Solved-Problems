class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        colunm = len(matrix[0])
        result = []


        for k in range(colunm):
            arr = []
            for w in range(row):
                arr.append(0)
            result.append(arr)


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result[j][i] = matrix[i][j] 
                
        return result
