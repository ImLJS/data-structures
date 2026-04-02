class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def explore(grid, r, c, visited):
            row_in = 0 <= r < len(grid)
            col_in = 0 <= c < len(grid[0])
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

            if not row_in or not col_in:
                return False
            
            if (r, c) in visited:
                return False
            
            if grid[r][c] == "0":
                return False
            
            visited.add((r,c))
            for x, y in directions:
                explore(grid, r+x, c+y, visited)
            
            return True

        ROWS = len(grid)
        COLS = len(grid[0])
        max_size = 0
        visited = set() # { (row, col) }

        for r in range(ROWS):
            for c in range(COLS):
                if explore(grid, r, c, visited):
                    max_size+=1
        
        return max_size
    

