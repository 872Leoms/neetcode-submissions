class Solution:
    import math
    def reverse(self, x: int) -> int:
        thelength = len(str(abs(x))) - 1
        multi = 10**(thelength)
        print(multi)
        res = 0
        while x:
            rem = math.fmod(x,10)
            x = int(x / 10)
            print(x)
            res += rem * multi
            thelength -= 1
            multi = 10 ** (thelength)
        if -2**(31) > int(res) or int(res) > 2**(31) - 1:
            return 0
        return int(res)

