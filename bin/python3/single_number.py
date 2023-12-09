class Solution:
    # 144ms
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        try:
            for i in range(0, len(nums), 2):
                if nums[i] != nums[i+1]:
                    return nums[i]
        except IndexError:
            return nums[i]
