func permute(nums []int) [][]int {
	var result [][]int
	backtrack(nums, 0, &result)
	return result
}

func backtrack(nums []int, start int, result *[][]int) {
	if start == len(nums) {
		perm := make([]int, len(nums))
		copy(perm, nums)
		*result = append(*result, perm)
		return
	}

	for i := start; i < len(nums); i++ {
		nums[start], nums[i] = nums[i], nums[start]
		backtrack(nums, start+1, result)
		nums[start], nums[i] = nums[i], nums[start]
	}
}

