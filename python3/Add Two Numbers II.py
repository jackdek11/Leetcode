# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two stacks to store the digits of l1 and l2
        stack_l1 = []
        stack_l2 = []

        # Traverse l1 and push its digits onto stack_l1
        while l1:
            stack_l1.append(l1)
            l1 = l1.next

        # Traverse l2 and push its digits onto stack_l2
        while l2:
            stack_l2.append(l2)
            l2 = l2.next

        carry = 0  # Carry value
        head = None  # Head of the resulting linked list

        # Iterate while either stack_l1 or stack_l2 is not empty
        while stack_l1 or stack_l2:
            # Get the value of the top digit from stack_l1 or 0 if stack_l1 is empty
            v1 = stack_l1.pop().val if stack_l1 else 0
            # Get the value of the top digit from stack_l2 or 0 if stack_l2 is empty
            v2 = stack_l2.pop().val if stack_l2 else 0

            # Calculate the sum of the digits and the carry
            v = v1 + v2
            carry, v = divmod(v + carry, 10)

            # Create a new ListNode with the current digit
            # and set it as the new head of the resulting linked list
            temp = head
            head = ListNode(v)
            head.next = temp

        # If there is a remaining carry, add a new ListNode for it
        if carry:
            temp = head
            head = ListNode(carry)
            head.next = temp

        return head