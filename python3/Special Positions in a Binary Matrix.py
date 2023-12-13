class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and all(mat[i][col] == 0 for col in range(n) if col != j) and all(mat[row][j] == 0 for row in range(m) if row != i):
                    count += 1

        return count