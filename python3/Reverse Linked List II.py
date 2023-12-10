# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Traverse to find the node just before the left position
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing from left to right
        current = prev.next
        next_node = current.next

        for _ in range(right - left):
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = current.next

        return dummy.next