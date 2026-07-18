# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec(node):
            if not node:
                return [True,0]
            else:
                maxx = 0
                x = rec(node.left) 
                y = rec(node.right) 
                print(x,y)
                if x[0] and y[0]:
                    temp = abs(x[1] - y[1])
                    if temp == 0 or temp == 1:
                        maxx = max(x[1],y[1])
                    else:
                        return [False,0]
                else:
                    return [False,0]
                return [True,maxx+1]
        return(rec(root)[0])
        