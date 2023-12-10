package main

import (
	"fmt"
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	if len(intervals) == 0 {
		return 0
	}

	// Sort intervals based on the end time
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	count := 0
	end := intervals[0][1]

	for i := 1; i < len(intervals); i++ {
		// If the current interval overlaps with the previous one
		if intervals[i][0] < end {
			count++ // Increment the count of overlapping intervals
		} else {
			end = intervals[i][1] // Update the end time
		}
	}

	return count
}