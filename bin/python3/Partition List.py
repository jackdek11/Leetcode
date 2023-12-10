# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to serve as the heads of the two partitions
        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        smaller_tail = smaller_dummy
        greater_tail = greater_dummy

        while head:
            if head.val < x:
                smaller_tail.next = head
                smaller_tail = smaller_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next

            head = head.next

        # Combine the two partitions
        greater_tail.next = None
        smaller_tail.next = greater_dummy.next

        return smaller_dummy.next