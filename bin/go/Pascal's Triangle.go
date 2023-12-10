func generate(numRows int) [][]int {
    if numRows == 0 {
		return [][]int{}
	}

	result := [][]int{{1}}

	for i := 1; i < numRows; i++ {
		prevRow := result[len(result)-1]
		newRow := []int{1}

		for j := 1; j < i; j++ {
			newRow = append(newRow, prevRow[j-1]+prevRow[j])
		}

		newRow = append(newRow, 1)
		result = append(result, newRow)
	}

	return result
}