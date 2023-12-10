func canCompleteCircuit(gas []int, cost []int) int {
	n := len(gas)
	totalGas := 0
	currentGas := 0
	startIndex := 0

	for i := 0; i < n; i++ {
		totalGas += gas[i] - cost[i]
		currentGas += gas[i] - cost[i]

		if currentGas < 0 {
			currentGas = 0
			startIndex = i + 1
		}
	}

	if totalGas >= 0 {
		return startIndex
	}
	return -1
}