class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsHasZero = set()
        colsHasZero = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowsHasZero.add(r)
                    colsHasZero.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in rowsHasZero or c in colsHasZero:
                    matrix[r][c] = 0
        
        