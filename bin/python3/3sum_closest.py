class Solution:
    # 2890ms
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[n - 1]
        for i in range(0, n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum <= target:
                    j += 1
                else:
                    k -= 1
                if abs(closest - target) > abs(current_sum - target):
                    closest = current_sum
        return closest
