class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 53ms
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        previous = dummy
        count = 0
        current = head
        while current is not None:
            count += 1
            if count % k == 0:
                previous = self.reverseList(previous, current.next)
                current = previous.next
            else:
                current = current.next
        return dummy.next 
        
        
    def reverseList(self, start, end):
        previous = start.next
        current = previous.next
        while current is not end:
            nextNode = current.next
            current.next = start.next
            start.next = current
            current = nextNode
        previous.next = end
        return previous