class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = [0,len(matrix)-1]
        column = [0,len(matrix[0])-1]
        ans = []
        w = 0
        while row[0] <= row[1] and column[0] <= column[1]:
            curr = row[0]
            for i in range(column[0],column[1]+1):
                ans.append(matrix[curr][i])

            if row[0] > row[1] or column[0] > column[1]:
                break

            row[0] += 1
            curr = column[1]
            for j in range(row[0],row[1]+1):
                ans.append(matrix[j][curr])
            
            if row[0] > row[1] or column[0] > column[1]:
                break

            column[1] -= 1
            curr = row[1]
            for k in range(column[1],column[0]-1,-1):
                ans.append(matrix[curr][k])
            
            if row[0] > row[1] or column[0] > column[1]:
                break
                
            row[1] -= 1
            curr = column[0]
            for w in range(row[1],row[0]-1,-1):
                ans.append(matrix[w][curr])
            column[0] += 1

        return ans
            

        
