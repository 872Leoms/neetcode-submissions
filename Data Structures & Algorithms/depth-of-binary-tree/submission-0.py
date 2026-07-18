# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dep(node):
            if not node.left and not node.right:
                return 1
            else:
                x = y = 0
                if node.left:
                    x = 1 + dep(node.left)
                if node.right:
                    y = 1 + dep(node.right)
                return max(x,y)
        return(dep(root))