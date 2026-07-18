# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node,state):
            if not node:
                return [float("-inf"),float("inf"),True]
            else:
                L = rec(node.left,state)
                R = rec(node.right,state)
                if not(L[0] < node.val and R[1] > node.val and L[2] and R[2]):
                    state = False
                maxx = max(R[0],node.val)
                minn = min(L[1],node.val)
                return [maxx,minn,state]
        return(rec(root,True)[2])

 

        