# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = deque([[root, 0]])
        res = []
        thestp = 0
        while stack:
            node, pos = stack.popleft()
            if pos == thestp:
                res.append(node.val)
                thestp += 1
            if node.right:
                stack.append([node.right,pos+1])
            if node.left:
                stack.append([node.left,pos+1])
        print(stack)
        return(res)

        