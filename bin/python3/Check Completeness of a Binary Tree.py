from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            # Base case: if no rootNode given, the tree is 'complete'
            return True

        # Construct an empty result list
        result = list()

        # Construct a deque, holding only the root node and it's level
        queue = deque([(root, 1)])  # deque > list, [optomized for pop / append]

        while queue:
            # Get the current node and level from the deque
            current_node, current_level = queue.popleft()
            
            # Add the 'level' to our result list
            result.append(current_level)
            
            # If the current node has children, add them to the deque
            # For left children, their 'level' is 2^x (2*2*2.. n times). 
            # With recursion, we already have x (current_level). The right 
            # child's 'level' is the same, plus 1.

            if current_node.left:
                queue.append((current_node.left, 2 * current_level))
            if current_node.right:
                queue.append((current_node.right, 2 * current_level + 1))
        
        # return if the number of nodes == the last leaf node's level
        return len(result) == result[-1]
