func strangePrinter(s string) int {
	n := len(s)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	for length := 1; length <= n; length++ {
		for i := 0; i <= n-length; i++ {
			j := i + length - 1
			if length == 1 {
				dp[i][j] = 1
			} else {
				dp[i][j] = length
				for k := i; k < j; k++ {
					if s[i] == s[k+1] {
						dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]-1)
					} else {
						dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
					}
				}
			}
		}
	}

	return dp[0][n-1]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}