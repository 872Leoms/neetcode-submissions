# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        total = 0
        def rec(node):
            nonlocal total
            if not node:
                return 0
            else:
                left = rec(node.left)
                right = rec(node.right)
                maxx = left + right
                if maxx > total:
                    total = maxx 
                return max(left,right) + 1
        rec(root)
        return(total)




        