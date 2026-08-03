class Node:
    def __init__(self,val = None,end = False):
        self.val = val
        self.end = end
        self.child = {}
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        allwords = set()
        def rec(i,j,node,seq):
            if node.end:
                allwords.add(seq)
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] == "#":
                return 
            temp = board[i][j] 
            board[i][j] = "#"
            if temp in node.child:
                seq += temp
                rec(i - 1,j,node.child[temp],seq)
                rec(i + 1,j,node.child[temp],seq)
                rec(i,j-1,node.child[temp],seq)
                rec(i,j+1,node.child[temp],seq)
            board[i][j] = temp
            return 




        root = Node("root")
        rows,cols = len(board),len(board[0])
        for i in words:
            head = root 
            for j in i:
                if j not in head.child:
                    head.child[j] = Node(j)
                head = head.child[j]
            head.end = True

        for a in range(rows):
            for b in range(cols):
                t = root
                if board[a][b] in t.child:
                    rec(a,b,t,"")
        return list(allwords)