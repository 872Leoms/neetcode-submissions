# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def rec(node,z):
            if not node:
                return [None,z]
            else:
                x = rec(node.left,z)
                z.append(node.val)
                y = rec(node.right,z)
                return [node,z]
        return(rec(root,[])[1][k-1])
        

        