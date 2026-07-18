# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur = [[root,0]]
        new = dict()
        res = []
        if not root:
            return []
        while cur:
            value,level = cur.pop()
            if level not in new:
                new[level] = [value.val]
            else:
                new[level]= new[level] + [(value.val)]
            if value.right:
                cur.append([value.right,level+1])
            if value.left:
                cur.append([value.left,level+1])
        for  i in new.keys():
            res.append(new[i])

        print(cur)
        print(new)
        return(res)
