class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(num,dic):
            if num == 0:
                print("we are in 0")
                return 1
            if num in dic:
                print("we are in dic")
                return dic[num]
            temp1 = 0
            if num - 2 > -1:
                print("we are in 2",num,dic)
                temp1 = rec(num - 2,dic)
            dic[num] = temp1 + rec(num - 1,dic)
            return temp1 + rec(num - 1,dic)
        return(rec(n,{}))

        