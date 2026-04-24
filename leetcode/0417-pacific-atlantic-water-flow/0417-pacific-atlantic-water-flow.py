class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        pas,alt = set(),set()

        def inbound(r,c):
            return 0 <= r < ROW and 0 <= c < COL
    
        def dfs(row,col,visted,prev):
            if not inbound(row,col) or (row,col) in visted or heights[row][col] < prev:
               return 

            visted.add((row,col))
            dfs(row + 1,col,visted,heights[row][col])
            dfs(row - 1,col,visted,heights[row][col])
            dfs(row,col + 1,visted,heights[row][col])
            dfs(row,col - 1,visted,heights[row][col])


        for r in range(ROW):
            dfs(r,0,pas,heights[r][0])
            dfs(r,COL-1,alt,heights[r][COL-1])

        for c in range(COL):
            dfs(0,c,pas,heights[0][c])
            dfs(ROW-1,c,alt,heights[ROW-1][c])


        ans = []
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in pas and (i,j) in alt:
                    ans.append([i,j])
                
        return ans