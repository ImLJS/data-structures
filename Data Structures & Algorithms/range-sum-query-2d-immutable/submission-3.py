class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix =  [ [0]*cols for _ in range(rows) ]
        for i in range(rows):
            curSum = 0
            for j in range(cols):
                curSum += matrix[i][j]
                self.prefix[i][j] = curSum

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