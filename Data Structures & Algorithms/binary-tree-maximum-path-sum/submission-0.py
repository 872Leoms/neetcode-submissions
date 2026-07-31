# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
            self.maximums = float("-inf")
            def rec(node):
                if not node:
                    return float("-inf")
                left = rec(node.left)
                right = rec(node.right)
                allvalue = left + right + node.val
                value = max(left + node.val,right + node.val ,node.val,allvalue)
                if value > self.maximums:
                    self.maximums = value
                return max(left + node.val,right + node.val ,node.val)
            rec(root)
            return self.maximums
            
