class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        direction = [(0,-1),(-1,0),(1,0),(0,1)]

        n = len(board)
        m = len(board[0])

        def inbound(r,c):
            return  0 <= r < n and 0 <= c < m

        def dfs(r,c):
            if not inbound(r,c):
                return 

            visted[r][c] = 1
            for dir in direction:
                new_r = r + dir[0]
                new_c = c + dir[1]

                if inbound(new_r,new_c) and not visted[new_r][new_c] and board[new_r][new_c] == 'O':
                     dfs(new_r,new_c)


        visted = [[0] * m for i in range(n)]
        row,col = 0,0

        
        for i in range(m):
            if board[row][col] == "O":
                dfs(row,col)
            col += 1
        col = m-1
        

        for i in range(n):
            if board[row][col] == "O":
                dfs(row,col)
            row += 1
        row = n -1

        for i in range(m-1,-1,-1):
            if board[row][col] == "O":
                dfs(row,col)
            col -= 1
            
        col = 0
        
        
        for i in range(n-1,-1,-1):
            if board[row][col] == "O":
                dfs(row,col)
            row -= 1

    
        for i in range(n):
            for j in range(m):
                if not visted[i][j]  and board[i][j] == "O":
                    board[i][j] = "X"