# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [[root,float('-inf')]]
        good = []
        while stack:
            node,value = stack.pop()
            maxx = value
            if node.val >= value:
                good.append(node.val)
                maxx = node.val
            if node.left:
                stack.append([node.left,maxx])
            if node.right:
                stack.append([node.right,maxx])
        return(len(good))


        