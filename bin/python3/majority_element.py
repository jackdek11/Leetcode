class Solution:
    # 444ms
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0 
        value = None
        possib_nums = set(nums)
        for num in possib_nums:
            val = nums.count(num)
            if val > answer:
                answer = val
                value = num
        return value
