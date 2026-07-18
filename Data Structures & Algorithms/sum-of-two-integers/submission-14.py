class Solution:
    def getSum(self, a: int, b: int) -> int: 
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        xo = (a^b) & mask
        an = (a & b) << 1
        while an:
            temp = xo
            xo = (xo ^ an) & mask
            an = (temp & an) << 1
        if xo <= max_int:
            print("here")
            return(xo)
        else:
            return ~(xo^mask)


