class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,-1),(-1,0),(0,1),(1,0)]
        n = len(grid)
        m = len(grid[0])

        def inbound(row,col):
            return 0 <= row < n and 0 <= col < m
            
        count = 0

        def dfs(row,col):
            if not inbound(row,col):
                return

            grid[row][col] = "0"
            for dirs in directions:
                r_new = row + dirs[0]
                c_new = col + dirs[1]
                if inbound(r_new,c_new) and  grid[r_new][c_new] == '1':
                    grid[r_new][c_new] = 0
                    dfs(r_new,c_new)

        for i in range(n):
            for j in range(m):
                if  grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
                
        return count

            
