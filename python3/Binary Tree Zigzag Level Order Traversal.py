class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        currLevel = []
        if root:
            currLevel.append(root)
        while currLevel:
            ret.append([node.val for node in currLevel])
            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel
        for i in range(1,len(ret),2):
            ret[i].reverse()
        return ret