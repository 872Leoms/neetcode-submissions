class Solution:
    def isHappy(self, n: int) -> bool:
        div = set()
        while n != 1:
            print(n)
            n = sum(int(digit)**2 for digit in str(n))
            if n in div:
                print("in div",div)
                return False
            div.add(n)
        return True
        