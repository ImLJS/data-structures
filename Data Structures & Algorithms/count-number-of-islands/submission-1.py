class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(grid, r, c, visited):
            row_in = 0 <= r < len(grid)
            col_in = 0 <= c < len(grid[0])
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            if not row_in or not col_in:
                return

            if grid[r][c] == "0":
                return
            
            if (r,c) in visited:
                return
            
            visited.add((r,c))

            for x,y in directions:
                explore(grid, r+x, c+y, visited)
            
            return

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        island = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    explore(grid, r, c, visited)
                    island+=1
        
        return island