class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS  = len(matrix)
        COLS  = len(matrix[0])
        self.prefix =  [ [0]*COLS for _ in range(ROWS) ]

        for i in range(ROWS):
            cur_sum = 0
            for j in range(COLS):
                cur_sum+=matrix[i][j]
                self.prefix[i][j] = cur_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2+1):
            left = self.prefix[r][col1-1] if col1>0 else 0
            right = self.prefix[r][col2]
            total+=(right-left)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)