class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])

        count = 0  # Number of intervals to remove
        end = intervals[0][1]  # Current end time

        for i in range(1, len(intervals)):
            # If the current interval overlaps with the previous one
            if intervals[i][0] < end:
                count += 1  # Increment the count of overlapping intervals
            else:
                end = intervals[i][1]  # Update the end time

        return count