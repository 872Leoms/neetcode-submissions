# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True
        o = [[p,q]]
        v = []
        while o:
            check = o.pop()
            if check[0] != check[1]:
                if not check[0] or not check[1]:
                    print(False)
                    return False
                if check[0].val == check[1].val:
                    o.append([check[0].left,check[1].left])
                    o.append([check[0].right,check[1].right])
                    v.append(check)       
                else:
                    return(False)
        return(True)
        