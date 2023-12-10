/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func levelOrderBottom(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	var result [][]int
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		levelSize := len(queue)
		levelValues := make([]int, levelSize)

		for i := 0; i < levelSize; i++ {
			node := queue[i]
			levelValues[i] = node.Val

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		result = append([][]int{levelValues}, result...)
		queue = queue[levelSize:]
	}

	return result
}