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
        stack = [[root,0]]
        dic =  dict()
        while stack:
            node,pos = stack.pop()
            if pos not in dic:
                dic[pos] = [node.val]
            else:
                dic[pos] += [node.val]
            if node.right:
                stack.append([node.right,pos+1])
            if node.left:
                stack.append([node.left,pos+1])
        for key in sorted(dic.keys()):
            stack.append(dic[key].pop())
        return(stack)

        