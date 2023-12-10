# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binary_search_left(low, high, target):
            while low < high:
                mid = (low + high) // 2
                if mountain_arr.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid
            return low if mountain_arr.get(low) == target else -1

        def binary_search_right(low, high, target):
            while low < high:
                mid = (low + high) // 2
                if mountain_arr.get(mid) > target:
                    low = mid + 1
                else:
                    high = mid
            return low if mountain_arr.get(low) == target else -1

        # Step 1: Find the peak element in the mountain array
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # Step 2: Perform binary search on the left and right sides of the peak
        left_result = binary_search_left(0, peak, target)
        right_result = binary_search_right(peak, n - 1, target)

        if left_result != -1:
            return left_result
        elif right_result != -1:
            return right_result
        else:
            return -1