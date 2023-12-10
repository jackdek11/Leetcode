package main

import (
	"fmt"
)

func findNumberOfLIS(nums []int) int {
	n := len(nums)
	if n <= 1 {
		return n
	}

	lengths := make([]int, n) // Initialize lengths to 1 for each number
	counts := make([]int, n)  // Initialize counts to 1 for each number

	for i := 0; i < n; i++ {
		lengths[i] = 1
		counts[i] = 1
	}

	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				if lengths[j]+1 > lengths[i] {
					lengths[i] = lengths[j] + 1
					counts[i] = counts[j]
				} else if lengths[j]+1 == lengths[i] {
					counts[i] += counts[j]
				}
			}
		}
	}

	maxLength := 0
	result := 0

	for i := 0; i < n; i++ {
		if lengths[i] > maxLength {
			maxLength = lengths[i]
			result = counts[i]
		} else if lengths[i] == maxLength {
			result += counts[i]
		}
	}

	return result
}