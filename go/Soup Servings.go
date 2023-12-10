func soupServings(n int) float64 {
	memo := make([][]float64, 192)
	for i := range memo {
		memo[i] = make([]float64, 192)
	}

	var dfs func(a, b int) float64
	dfs = func(a, b int) float64 {
		if a <= 0 && b <= 0 {
			return 0.5
		}
		if a <= 0 {
			return 1.0
		}
		if b <= 0 {
			return 0.0
		}
		if memo[a][b] > 0 {
			return memo[a][b]
		}

		memo[a][b] = 0.25 * (dfs(a-4, b) +
			dfs(a-3, b-1) +
			dfs(a-2, b-2) +
			dfs(a-1, b-3))
		return memo[a][b]
	}

	// Adjust the initial amount of soup
	adjustedN := (n + 24) / 25

	if adjustedN >= 192 {
		return 1.0 // As n >= 4800, the probability is 1.0
	}

	return dfs(adjustedN, adjustedN)
}