/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}

	// The first element in preorder is the root of the current subtree
	rootVal := preorder[0]
	root := &TreeNode{Val: rootVal}

	// Find the index of the root in the inorder list
	var rootIndex int
	for i, val := range inorder {
		if val == rootVal {
			rootIndex = i
			break
		}
	}

	// Recursively construct left and right subtrees
	root.Left = buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])
	root.Right = buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])

	return root
}

// Helper function to perform inorder traversal for verification
func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	var result []int
	result = append(result, inorderTraversal(root.Left)...)
	result = append(result, root.Val)
	result = append(result, inorderTraversal(root.Right)...)
	return result
}