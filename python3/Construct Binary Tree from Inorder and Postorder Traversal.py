# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = postorder[-1]
        inorder_root_index = inorder.index(root)
        left_inorder = inorder[:inorder_root_index]
        right_inorder = inorder[inorder_root_index+1:]
        left_postorder = postorder[:inorder_root_index]
        right_postorder = postorder[inorder_root_index:-1]
        root = TreeNode(root)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root