class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # 39ms
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            temp = list1
            temp.next = self.mergeTwoLists(list1.next, list2)
        else:
            temp = list2
            temp.next = self.mergeTwoLists(list1, list2.next)
        return temp
