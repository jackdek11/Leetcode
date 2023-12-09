class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            # Base case. If no root, output in 0
            return 0

        level = 0
        arr = list()

        def dfs(root: TreeNode, level: int) -> None:
            """
            Depth-first search. Use dfs to add up TreeNode values. 'res' represents
            the level of the tree traversal
            """
            if not root:
                return None
            if not root.left and not root.right:
                arr.append(level+root.val)
                return None

            dfs(root.left, (level+root.val)*10)
            dfs(root.right, (level+root.val)*10)

        dfs(root, level)
        return sum(arr)