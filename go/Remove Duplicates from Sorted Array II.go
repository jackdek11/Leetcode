package main

import "fmt"

func removeDuplicates(nums []int) int {
	n := len(nums)
	if n <= 2 {
		return n
	}

	// Count to keep track of the number of occurrences of the current element
	count := 1

	// Pointer to track the position where the next unique element should be placed
	pos := 1

	for i := 1; i < n; i++ {
		if nums[i] == nums[i-1] {
			count++
		} else {
			count = 1
		}

		// If the count is less than or equal to 2, copy the element to the next position
		if count <= 2 {
			nums[pos] = nums[i]
			pos++
		}
	}

	return pos
}
