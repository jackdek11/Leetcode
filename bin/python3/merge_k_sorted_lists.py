class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 292ms
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        return self.mergeLists(lists, 0, len(lists) - 1)

    def mergeLists(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeLists(lists, start, mid)
        right = self.mergeLists(lists, mid + 1, end)
        return self.merge(left, right)

    @staticmethod
    def merge(left, right):
        head = ListNode(-1)
        temp = head
        while left is not None and right is not None:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        while left is not None:
            temp.next = left
            left = left.next
            temp = temp.next
        while right is not None:
            temp.next = right
            right = right.next
            temp = temp.next
        return head.next
