class Solution:
    # 157ms
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = dict()
        for index, value in enumerate(nums):
            ans = target - value
            if ans in elements:
                return [elements[ans], index]
            elements[value] = index
        return []
