package main

func knightProbability(n, k, row, column int) float64 {
	// Possible knight moves
	moves := [8][2]int{{-2, -1}, {-1, -2}, {-2, 1}, {-1, 2}, {1, -2}, {2, -1}, {1, 2}, {2, 1}}

	// Initialize a 3D memoization table to store the probabilities
	dp := make([][][]float64, k+1)
	for i := range dp {
		dp[i] = make([][]float64, n)
		for j := range dp[i] {
			dp[i][j] = make([]float64, n)
		}
	}

	// Base case: probability of starting position (k=0) is 1
	dp[0][row][column] = 1.0

	// Dynamic programming to calculate probabilities
	for step := 1; step <= k; step++ {
		for r := 0; r < n; r++ {
			for c := 0; c < n; c++ {
				for _, move := range moves {
					nr, nc := r+move[0], c+move[1]
					if nr >= 0 && nr < n && nc >= 0 && nc < n {
						dp[step][r][c] += dp[step-1][nr][nc] / 8.0
					}
				}
			}
		}
	}

	// Sum all probabilities for all cells on the chessboard after k moves
	var probability float64
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			probability += dp[k][r][c]
		}
	}

	return probability
}