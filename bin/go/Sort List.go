/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func sortList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
		return head
	}

	mid := findMiddle(head)
	left := head
	right := mid.Next
	mid.Next = nil

	leftSorted := sortList(left)
	rightSorted := sortList(right)

	return merge(leftSorted, rightSorted)
}

func findMiddle(head *ListNode) *ListNode {
	slow, fast := head, head
	var prev *ListNode

	for fast != nil && fast.Next != nil {
		prev = slow
		slow = slow.Next
		fast = fast.Next.Next
	}

	return prev
}

func merge(left *ListNode, right *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	for left != nil && right != nil {
		if left.Val < right.Val {
			curr.Next = left
			left = left.Next
		} else {
			curr.Next = right
			right = right.Next
		}
		curr = curr.Next
	}

	if left != nil {
		curr.Next = left
	} else {
		curr.Next = right
	}

	return dummy.Next
}