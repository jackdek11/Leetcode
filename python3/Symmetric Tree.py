# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        stack = []
        stack.append(root.right)
        stack.append(root.left)
        
        while(stack):
            leftNode = stack.pop()
            rightNode = stack.pop()
            
            if leftNode == None and rightNode == None:
                continue
                
            if leftNode == None or rightNode == None or (leftNode.val != rightNode.val):
                return False
            
            stack.append(leftNode.left)
            stack.append(rightNode.right)
            
            stack.append(leftNode.right)
            stack.append(rightNode.left)
            
        return True