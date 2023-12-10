/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return []*TreeNode{}
	}
	return generateTreeHelper(1, n)
}

func generateTreeHelper(start, end int) []*TreeNode {
	trees := []*TreeNode{}

	if start > end {
		trees = append(trees, nil)
		return trees
	}

	for i := start; i <= end; i++ {
		leftTrees := generateTreeHelper(start, i-1)
		rightTrees := generateTreeHelper(i+1, end)

		for _, left := range leftTrees {
			for _, right := range rightTrees {
				root := &TreeNode{Val: i}
				root.Left = left
				root.Right = right
				trees = append(trees, root)
			}
		}
	}

	return trees
}
