# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            nonlocal prev, max_freq, curr_freq, modes

            if not node:
                return

            inorder(node.left)

            if node.val == prev:
                curr_freq += 1
            else:
                curr_freq = 1

            if curr_freq == max_freq:
                modes.append(node.val)
            elif curr_freq > max_freq:
                max_freq = curr_freq
                modes = [node.val]

            prev = node.val

            inorder(node.right)

        prev = None
        max_freq = 0
        curr_freq = 0
        modes = []

        inorder(root)

        return modes