class Solution:
    # 32ms
    def removeElement(self, nums: List[int], val: int) -> List[int]:        
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count