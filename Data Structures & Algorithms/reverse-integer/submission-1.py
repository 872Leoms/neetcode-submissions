class Solution:
    def reverse(self, x: int) -> int:
        temp = int(str(abs(x))[::-1])
        if x < 0:
            temp = -temp
        if temp < -(1 << 31) or temp > (1 << 31) - 1:
            return 0
        return temp