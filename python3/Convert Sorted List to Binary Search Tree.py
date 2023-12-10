class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        slow, fast = head, head
        prev_slow = None

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        if slow == head:
            return root

        prev_slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root