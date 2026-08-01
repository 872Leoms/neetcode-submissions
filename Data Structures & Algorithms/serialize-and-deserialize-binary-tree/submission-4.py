from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        res = ""
        while queue:
            value = queue.popleft()
            if value:
                left = value.left
                right = value.right
                queue.append(value.left)
                queue.append(value.right)
            temp = value.val if value else None
            res += str(temp) + "#"
        print(res)
        return res      
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        temp = data.strip("#").split("#")
        if temp[0] == "None" or len(temp) == 0:
            return None
        head = TreeNode(temp[0])
        if len(temp) == 1:
            return head
        queue = deque([head])
        temp = temp[1:]
        while queue:
            parent = queue.popleft()
            left = temp.pop(0)
            nodeleft = TreeNode(left) if left != "None" else None
            right = temp.pop(0)
            noderight = TreeNode(right) if right != "None" else None
            if nodeleft:          
                queue.append(nodeleft)
            if noderight:
                queue.append(noderight)
            parent.left = nodeleft
            parent.right = noderight
        return head


