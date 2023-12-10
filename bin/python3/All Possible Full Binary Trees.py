# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode(0)]

        result = []
        for i in range(1, n, 2):  # Iterate over odd numbers up to n-1
            left_subtrees = self.allPossibleFBT(i)
            right_subtrees = self.allPossibleFBT(n - i - 1)

            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)

        return result