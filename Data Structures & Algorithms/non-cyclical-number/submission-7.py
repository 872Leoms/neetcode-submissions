class Solution:
    def isHappy(self, n: int) -> bool:
        p1 = n
        p2 = n
        while p2 != 1:
            p1 = sum(int(digit)**2 for digit in str(p1))
            for i in range(2):
                p2 = sum(int(digit)**2 for digit in str(p2))
            if p1 == p2 and p1 != 1:
                return False
        return True
        