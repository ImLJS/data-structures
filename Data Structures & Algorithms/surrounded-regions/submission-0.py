class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def explore(r,c):
            row_in = 0 <= r < ROWS
            col_in = 0 <= c < COLS

            if not row_in or not col_in or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            explore(r+1,c)
            explore(r-1,c)
            explore(r,c-1)
            explore(r,c+1)

        for r in range(ROWS):
            if board[r][0] == '0':
                explore(r,c)
            if board[r][COLS-1] == '0':
                explore(r,c)
        
        for c in range(COLS):
            if board[0][c] == '0':
                explore(r,c)
            if board[ROWS-1][c] == '0':
                explore(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
