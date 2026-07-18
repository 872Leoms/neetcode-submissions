# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        temp = {}
        for i in range(len(inorder)):
            temp[inorder[i]] = i
        pre= 0
        def rec(s,e,dic):
            nonlocal pre
            if s > e:
                return None
            else:
                myroot = TreeNode(preorder[pre],None,None)
                pre += 1
                myrootindex = dic[myroot.val]
                myroot.left = rec(s,myrootindex-1,dic)
                myroot.right = rec(myrootindex+1,e,dic)
                return myroot

        return rec(0,len(preorder)-1,temp)

