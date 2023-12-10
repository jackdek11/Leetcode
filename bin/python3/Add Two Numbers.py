class Solution:
    # 168ms
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        carry = 0
        
        res = None
        prev = None
        
        while l1 is not None or l2 is not None:
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = (1 if sum >= 10 else 0)
            sum = sum % 10
            temp = ListNode(sum)
            if res is None:
                res = temp
            else:
                prev.next = temp
            prev = temp
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            temp.next = ListNode(carry)
        return res
