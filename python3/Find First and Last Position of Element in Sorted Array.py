class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findFirstOccurrence(nums, target), self.findLastOccurrence(nums, target)]
        
    @staticmethod
    def findLastOccurrence(nums, target):
        left, right = 0, len(nums) - 1
        lastOccurrence = -1
        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                lastOccurrence = middle
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return lastOccurrence
    

    @staticmethod
    def findFirstOccurrence(nums, target):
        left, right = 0, len(nums) - 1
        firstOccurrence = -1
        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                firstOccurrence = middle
                right = middle - 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return firstOccurrence