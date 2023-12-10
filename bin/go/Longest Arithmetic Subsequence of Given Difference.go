func longestSubsequence(arr []int, difference int) int {
	ans := 0
	lengthAt := make(map[int]int)

	for _, a := range arr {
		lengthAt[a] = lengthAt[a-difference] + 1
		ans = max(ans, lengthAt[a])
	}

	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}