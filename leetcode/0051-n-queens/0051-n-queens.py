class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        

        def recur(board,row):
            if row == n:
                res.append(deepcopy(board))
                return 
            for i in range(n):
                if board[row][i] == 0:
                    board[row][i] = "Q"

                    for j in range(n):
                        for k in range(n):
                            if j != row or k != i:
                                if j == row or k == i or (j-k) == (row- i) or (j+k) == (row+i):
                                    board[j][k] += 1
                        
                    recur(board,row + 1)
                    board[row][i] = 0

                    for j in range(n):
                        for k in range(n):
                            if j != row or k != i:
                                if j == row or k == i or (j-k) == (row- i) or (j+k) == (row+i):
                                    board[j][k] -=1

        recur([[0] * n  for i in range(n)],0)
        ans = []
        for i in range(len(res)):
            arr = []
            for j in range(n):
                for k in range(n):
                    if res[i][j][k] != "Q":
                        res[i][j][k] = "."
                    
                arr.append("".join(res[i][j]))
            ans.append(arr)

        return ans

