class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0

        DIRECTION = "RIGHT"

        RIGHT_WALL = cols
        DOWN_WALL = rows
        LEFT_WALL = -1
        UP_WALL = 0

        while len(res) != rows*cols:

            if DIRECTION == "RIGHT":
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j+=1
                i, j = i+1, j-1
                DIRECTION = "DOWN"
                RIGHT_WALL -=1
            elif DIRECTION == "DOWN":
                while i < DOWN_WALL:
                    res.append(matrix[i][j])
                    i+=1
                i, j = i-1, j-1
                DIRECTION = "LEFT"
                DOWN_WALL -=1
            
            elif DIRECTION == "LEFT":
                while j>LEFT_WALL:
                    res.append(matrix[i][j])
                    j-=1
                i, j = i - 1, j + 1
                DIRECTION = "UP"
                LEFT_WALL += 1
            else:
                while i>UP_WALL:
                    res.append(matrix[i][j])
                    i-=1
                i, j = i + 1, j + 1
                DIRECTION = "RIGHT"
                UP_WALL +=1
        return res


















        