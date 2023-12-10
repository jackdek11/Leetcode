func numberOfMatches(n int) int {
	matches := 0

	for n > 1 {
		if n%2 == 0 {
			matches += n / 2
			n /= 2
		} else {
			matches += (n - 1) / 2
			n = (n - 1) / 2 + 1
		}
	}

	return matches
}