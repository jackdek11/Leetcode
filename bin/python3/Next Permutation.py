class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                break
        if index == -1:
            self.reverse(nums, 0, n - 1)
            return
        j = n - 1
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                j = i
                break
        nums[index], nums[j] = nums[j], nums[index]
        self.reverse(nums, index + 1, n - 1)
    
    @staticmethod
    def reverse(nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1