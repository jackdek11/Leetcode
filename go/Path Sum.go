/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil {
        return false
    }

    // Check if the current node is a leaf node and its value equals the remaining target sum
    if root.Left == nil && root.Right == nil && root.Val == targetSum {
        return true
    }

    // Recur for the left and right subtrees
    return hasPathSum(root.Left, targetSum-root.Val) || hasPathSum(root.Right, targetSum-root.Val)
}