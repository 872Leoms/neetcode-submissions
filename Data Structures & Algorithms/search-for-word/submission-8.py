class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,columns = len(board),len(board[0])
        unique = set()
        def rec(word,ind,i,j):        
            if ind == len(word):
                print("we reach")
                return True

            if (i,j) in unique:
                return False
            if 0 > i or i >= rows or 0 > j or j >= columns:
                return False
            if word[ind] != board[i][j]:
                return False

            left,right,top,bottom = False,False,False,False
            unique.add((i,j))

            left = rec(word,ind+1,i,j-1)
            right = rec(word,ind+1,i,j+1)
            top = rec(word,ind+1,i-1,j)
            bottom = rec(word,ind+1,i+1,j)
            
            stat = left or right or top or bottom
            unique.remove((i,j))              
            return stat

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    if (rec(word,0,i,j)):
                        return True
        return False
        


