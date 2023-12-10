class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible knight moves
        moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

        # Initialize a 3D memoization table to store the probabilities
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]

        # Base case: probability of starting position (k=0) is 1
        dp[0][row][column] = 1

        # Dynamic programming to calculate probabilities
        for step in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            dp[step][r][c] += dp[step - 1][nr][nc] / 8.0

        # Sum all probabilities for all cells on the chessboard after k moves
        probability = sum(sum(dp[k][r][c] for r in range(n)) for c in range(n))

        return probability