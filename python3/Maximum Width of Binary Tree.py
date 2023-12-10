from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            level_size = len(queue)
            _, level_start = queue[0]
            
            for _ in range(level_size):
                node, col_index = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2*col_index))
                if node.right:
                    queue.append((node.right, 2*col_index + 1))
            
            max_width = max(max_width, col_index - level_start + 1)
        
        return max_width