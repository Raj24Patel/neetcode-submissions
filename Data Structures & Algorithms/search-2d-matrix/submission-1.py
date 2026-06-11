class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l , r  = 0, ROWS * COLS -1

        while l <= r:#0, 11
            m = l + (r-l) // 2 # 5
            rows = m // COLS # 5 // 4 = 1
            cols = m % COLS # 5 % 4 = 1
            if matrix[rows][cols] > target:
                r = m - 1
            elif matrix[rows][cols] < target:
                l = m + 1
            else:
                return True

        
        return False
        