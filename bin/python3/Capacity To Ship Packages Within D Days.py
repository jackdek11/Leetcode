class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + right >> 1
            if self.findDays(weights, days, mid):
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findDays(self, weights: List[int], D: int, capacity) -> bool:
        weight_sum = 0
        days = 1
        for w in weights:
            weight_sum += w
            if weight_sum > capacity:
                days += 1
                weight_sum = w
        return days > D
