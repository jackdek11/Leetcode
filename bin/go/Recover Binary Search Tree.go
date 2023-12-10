/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func recoverTree(root *TreeNode) {
	var pre, first, second, maxRight *TreeNode
	for root != nil {
		if root.Left != nil {
			maxRight = root.Left
			for maxRight.Right != nil && maxRight.Right != root {
				maxRight = maxRight.Right
			}
			if maxRight.Right != root {
				maxRight.Right = root
				root = root.Left
			} else {
				maxRight.Right = nil
				if maxRight != nil && maxRight.Val > root.Val {
					if first == nil {
						first = maxRight
					}
					second = root
				}
				pre = root
				root = root.Right
			}
		} else {
			if pre != nil && pre.Val > root.Val {
				if first == nil {
					first = pre
				}
				second = root
			}
			pre = root
			root = root.Right
		}
	}
	first.Val, second.Val = second.Val, first.Val
}