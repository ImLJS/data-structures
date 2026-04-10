class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            nums = set()
            for col in range(9):
                if board[row][col].isdigit():
                    if board[row][col] in nums:
                        return False
        
        for col in range(9):
            nums = set()
            for row in range(9):
                if board[row][col].isdigit():
                    if board[row][col] in nums:
                        return False
        
        for col in range(0, 7, 3):
            for row in range(0, 7, 3):
                i_nn = board[row][col:col+3] + board[row+1][col:col+3] + board[row+2][col:col+3]
                # Filter out non-digit entries (only actual numbers matter, ignore '.')
                nn = []
                for w in i_nn:
                    if w.isdigit():
                        nn.append(w)
                # If duplicates exist among the digits, the board is invalid
                if len(nn) != len(set(nn)):
                    return False
        return True


        