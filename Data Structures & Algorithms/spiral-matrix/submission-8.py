class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        dip = 0
        lengr = n - 1
        lengc = m - 1
        count = 0 
        res = []
        while count < n * m:
            for i in range(dip,m - dip):
                res.append(matrix[dip][i])
                count += 1
            if count == n*m:
                break
            for i in range(dip+1,n - dip):
                res.append(matrix[i][lengc - dip])
                count += 1
            if count == n*m:
                break
            for i in range(lengc - dip - 1,dip - 1,-1):
                res.append(matrix[lengr - dip][i])
                count += 1
            if count == n*m:
                break
            for i in range(lengr - 1 - dip,dip,-1):
                res.append(matrix[i][dip])
                count += 1
            if count == n*m:
                break
            dip += 1
        return(res)
            

        