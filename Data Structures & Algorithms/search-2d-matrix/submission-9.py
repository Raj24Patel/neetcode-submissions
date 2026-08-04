class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) # 3
        cols = len(matrix[0]) #4
        l = 0
        r = cols * rows - 1 # 2

        while l <= r:
            m = l + ((r - l) // 2) #1

            ROWS = m // cols #column in row | 1 // 3
            COLS = m % cols# row in list[list] | 1 % 3

            if matrix[ROWS][COLS] < target:
                l = m + 1
            elif matrix[ROWS][COLS] > target:
                r = m - 1
            else:
                return True
        
        return False


        