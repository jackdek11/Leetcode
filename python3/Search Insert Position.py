class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        startInd = 0
        endInd = len(nums)-1
        medianInd = 0
        while (startInd <= endInd):
            medianInd = startInd + (endInd-startInd)//2
            
            if nums[medianInd] == target:
                return medianInd
            elif nums[medianInd] > target:
                endInd = medianInd - 1
            else:
                startInd = medianInd + 1
        
        return startInd
        