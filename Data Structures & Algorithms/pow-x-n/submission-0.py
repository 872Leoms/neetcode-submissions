class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if n < 0:
            neg = True
            n = -n
        def rec(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1
            temp = rec(x,n//2) 
            if n % 2 != 0:
                return temp * temp * x
            return temp*temp
        value = (rec(x,n))
        if neg:
            value = 1/value
        return value

        