class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 << 31
        print(bin(res))
        for i in range(31,-1,-1):
            temp = n & 1
            res = res | (temp << i)
            n = n >> 1
        return(res)
        print(bin(res))

        