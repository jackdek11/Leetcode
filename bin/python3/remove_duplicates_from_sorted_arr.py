class Solution(object):
    # 128ms
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return n
        temp = list(range(n))
        j = 0
        for i in range(0, n-1):
            if nums[i] != nums[i+1]:
                temp[j] = nums[i]
                j += 1
        temp[j] = nums[n-1]
        j += 1
        for i in range(0, j):
            nums[i] = temp[i]
        return j
