class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        # check if first row or first column has zeros
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break

        # use first row and first column as flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set zeros for rows and columns except first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # set zeros for first row and first column if needed
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0