/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func pathSum(root *TreeNode, targetSum int) [][]int {
	var result [][]int
	var currentPath []int
	findPaths(root, targetSum, &currentPath, &result)
	return result
}

func findPaths(node *TreeNode, remainingSum int, currentPath *[]int, result *[][]int) {
	if node == nil {
		return
	}

	*currentPath = append(*currentPath, node.Val)
	if node.Left == nil && node.Right == nil && remainingSum == node.Val {
		// This is a leaf node and the sum matches the targetSum
		pathCopy := make([]int, len(*currentPath))
		copy(pathCopy, *currentPath)
		*result = append(*result, pathCopy)
	}

	findPaths(node.Left, remainingSum-node.Val, currentPath, result)
	findPaths(node.Right, remainingSum-node.Val, currentPath, result)

	*currentPath = (*currentPath)[:len(*currentPath)-1] // Backtrack by removing the last element
}