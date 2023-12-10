class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize the slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Detect the intersection point of the two pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the "entrance" to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
