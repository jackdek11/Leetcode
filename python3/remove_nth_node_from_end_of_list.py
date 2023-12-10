class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 83ms
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for i in range(0, n):
            if fast.next is None:
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow.next is not None:
            slow.next = slow.next.next
        return head
