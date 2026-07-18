class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        keep = set()
        def rec(i,j):
            if i >= rows or i < 0 or j >= cols or j < 0:
                return
            else:
                if (i,j) in keep or board[i][j] == "X":
                    return
                keep.add((i,j))
                rec(i,j-1)
                rec(i,j+1)
                rec(i+1,j)
                rec(i-1,j)
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    if board[i][j] == "O" and ((i,j) not in keep):
                        print(f"i,j = {i,j}")
                        rec(i,j)
        for i in range(rows):
            for j in range(cols):
                if (i,j) in keep:
                    continue
                else:
                    board[i][j] = "X"
