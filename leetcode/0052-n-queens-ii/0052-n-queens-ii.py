class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []

        def recur(board,row):
            if row == n:
                ans.append(deepcopy(board))
                return 

            for i in range(n):
                if board[row][i] == 0:
                    board[row][i] = "Q"

                    for j in range(n):
                        for k in range(n):
                            if j != row or k != i:
                                if j == row or k == i or (j-k) == (row-i) or (j+k) == (row+i):
                                    board[j][k] += 1

                    recur(board,row+1)
                    board[row][i] = 0
                    
                    for j in range(n):
                        for k in range(n):
                            if j != row or k != i:
                                if j == row or k == i or (j-k) == (row-i) or (j+k) == (row+i):
                                    board[j][k] -= 1

        recur([[0]*n for i in range(n)],0)

        return len(ans)

        
