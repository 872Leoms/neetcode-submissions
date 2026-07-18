class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        div = [[-1]*n for _ in range(m)]
        div[m-1][n-1] = 1
        print(div)
        def rec(i,j):
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            print(i,j)
            if div[i][j] != -1:
                return div[i][j]
            right = rec(i,j+1)
            botoom = rec(i+1,j)
            total = right + botoom
            div[i][j] = total
            return total
        return(rec(0,0)) 