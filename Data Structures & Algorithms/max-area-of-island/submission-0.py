class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def explore(grid, r, c, visited):
            row_in = 0 <= r < len(grid) 
            col_in = 0 <= c < len(grid[0]) 

            if not row_in or not col_in:
                return 0
            if (r,c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
            
            visited.add((r,c))

            directions = [(1,0), (-1,0), (0, 1), (0,-1)]
            return 1 + explore(grid, r+1, c, visited) + explore(grid, r-1, c, visited) + explore(grid, r, c-1, visited) + explore(grid, r, c+1, visited)
            
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        visited = set() # { (row, col) }

        for r in range(ROWS):
            for c in range(COLS):
                size = explore(grid, r, c, visited)
                max_area = max(max_area, size)
        
        return max_area
