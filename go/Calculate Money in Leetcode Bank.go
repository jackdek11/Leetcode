func trapezoidSum(a, b int) int {
	// Returns sum(a..b).
	return (a + b) * (b - a + 1) / 2
}

func totalMoney(n int) int {
	weeks := n / 7
	firstWeek := trapezoidSum(1, 7)
	lastFullWeek := trapezoidSum(1+weeks-1, 7+weeks-1)
	remainingDays := trapezoidSum(1+weeks, n%7+weeks)
	return (firstWeek + lastFullWeek) * weeks / 2 + remainingDays
}