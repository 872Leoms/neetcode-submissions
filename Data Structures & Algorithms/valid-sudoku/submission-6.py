class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def coulmncheck(x):
            temp = dict()
            for i in range(9):
                for j in x:
                    if i not in temp:
                        temp[i] = str(j[i])
                    else:
                        temp[i] += str(j[i])
            for i in temp.values():
                clean = ""
                for j in i:
                    if j != ".":
                        clean += j
                if len(clean) != len(set(clean)):
                    return False
            return True
        def rowcheck(x):
            temp = dict()
            for i in x:
                for j in i:
                    if j not in temp:
                        temp[j] = 1
                    else:
                        temp[j] += 1
                for k,v in temp.items():
                    if v > 1 and k != ".":
                        return False
                temp = {}         
            return True
        def boxcheck(x):
            temp = dict()
            for i in range(9):
                col = i //3
                for j in range(9):
                    row = j // 3
                    if (str(col) + str(row)) not in temp:
                        temp[str(col) + str(row)] = str(x[i][j])
                    else:
                        temp[str(col) + str(row)] += str(x[i][j])
            for i in temp.values():
                clean = ""
                for j in i:
                    if j != ".":
                        clean += j
                if len(clean) > 0:
                   if len(clean) != len(set(clean)):
                       return False
            return True
        if rowcheck(board) and coulmncheck(board) and boxcheck(board):
            return True
        else:
            return False

        
        