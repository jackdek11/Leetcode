var digitToLetters = map[rune]string{
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
}

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return nil
	}

	var combinations []string
	var backtrack func(index int, currentCombination string)

	backtrack = func(index int, currentCombination string) {
		if index == len(digits) {
			combinations = append(combinations, currentCombination)
			return
		}

		digit := rune(digits[index])
		letters := digitToLetters[digit]
		for _, letter := range letters {
			backtrack(index+1, currentCombination+string(letter))
		}
	}

	backtrack(0, "")
	return combinations
}