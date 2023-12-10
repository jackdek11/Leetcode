class Solution:
    # 2970ms
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        nums_length = len(nums)
        if nums is None or nums_length < 4:
            return quadruplets
        nums.sort()
        for i in range(0, nums_length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, nums_length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = nums_length- 1
                while k < l:
                    current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if current_sum < target:
                        k += 1
                    elif current_sum > target:
                        l -= 1
                    else:
                        quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return quadruplets
