class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 96ms
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None): 
            return
        if (head.next != None): 
            if (head.val == head.next.val): 
                to_free = head.next
                head.next = head.next.next
                self.deleteDuplicates(head) 
            else: 
                self.deleteDuplicates(head.next)
        return head
