class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        temp = n
        for i in range(32):
            if temp & 1:
                res += 1
            temp = temp >> 1
        return(res)
