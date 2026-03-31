class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS*COLS-1

        while left<=right:
            mid = left + ((right-left)//2)
            i = mid//COLS
            j = mid%COLS

            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] > target:
                right = mid-1
            else:
                left = mid+1
        return False