/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return nil
    }

    res := [][]int{}
    queue := []*TreeNode{root}

    for len(queue) > 0 {
        level := []int{}
        levelSize := len(queue)

        for i := 0; i < levelSize; i++ {
            node := queue[0]
            queue = queue[1:]

            level = append(level, node.Val)

            if node.Left != nil {
                queue = append(queue, node.Left)
            }

            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }

        res = append(res, level)
    }

    return res
}
