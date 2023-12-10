/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func preorderTraversal(root *TreeNode) []int {
	result := []int{}
	  preorderRecursive(root, &result)
	  return result
  }
  
  func preorderRecursive(root *TreeNode, result *[]int) {
	  if root == nil {
		  return
	  }
	  *result = append(*result, root.Val)
	  preorderRecursive(root.Left, result)
	  preorderRecursive(root.Right, result)
  }
  