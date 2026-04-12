class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows*cols

        left, right = 0, n-1

        while left<=right:
            mid = (left+right)//2

            cur = matrix[mid//cols][mid%cols]

            if cur == target:
                return True
            
            elif cur > target:
                right = mid-1
            else:
                left = mid+1
        return False