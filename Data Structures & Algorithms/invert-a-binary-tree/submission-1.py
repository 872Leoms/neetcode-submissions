# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        op = [root]
        vis = []
        while op:
            cur = op[0]
            op = op[1:]
            if not cur:
                continue
            op.append(cur.right)
            op.append(cur.left)
            cur.left,cur.right = cur.right,cur.left
        return(root)


        