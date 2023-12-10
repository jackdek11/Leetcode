func partition(s string) [][]string {
	var partitions [][]string

	isPalindrome := func(substring string) bool {
		i, j := 0, len(substring)-1
		for i < j {
			if substring[i] != substring[j] {
				return false
			}
			i++
			j--
		}
		return true
	}

	var backtrack func(start int, path []string)
	backtrack = func(start int, path []string) {
		if start == len(s) {
			// Add a copy of the current path to the partitions.
			temp := make([]string, len(path))
			copy(temp, path)
			partitions = append(partitions, temp)
			return
		}

		for end := start + 1; end <= len(s); end++ {
			substring := s[start:end]
			if isPalindrome(substring) {
				path = append(path, substring)
				backtrack(end, path)
				path = path[:len(path)-1] // Remove the last element for backtracking
			}
		}
	}

	backtrack(0, []string{})
	return partitions
}