from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_seen = set()
        a_seen = set()
        p_queue = deque([])
        a_queue = deque([])
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1), (1, 0), (-1,0)]

        # Pacific Top Row
        for c in range(cols):
            p_seen.add((0, c))
            p_queue.append((0, c))
        
        # Pacific Left Column
        for r in range(1, rows):
            p_seen.add((r, 0))
            p_queue.append((r, 0))
        
        # Atlantic Bottom Row
        for c in range(cols):
            a_seen.add((rows-1,c))
            a_queue.append((rows-1,c))

        # Atlantic Right Column                    
        for r in range(rows-1):
            a_seen.add((r, cols-1))
            a_queue.append((r, cols-1))

        def isInbound(r,c):
            row_in = 0 <= r < rows 
            col_in = 0 <= c < cols 
            return row_in and col_in
        
        def bfs(queue, seen):
            while queue:
                r,c = queue.popleft()
                cur_height = heights[r][c]

                for x, y in directions:
                    new_row, new_col = r+x, c+y
                    if (new_row, new_col) not in seen and isInbound(new_row, new_col) and heights[new_row][new_col] >= cur_height:
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col))

        bfs(p_queue, p_seen)
        bfs(a_queue, a_seen)
        print(p_seen.intersection(a_seen))
        
        return list(p_seen.intersection(a_seen))
        