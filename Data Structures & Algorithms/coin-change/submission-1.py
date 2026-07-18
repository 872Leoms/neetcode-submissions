class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic = {}
        def rec(amount,dic):
            if amount == 0:
                return 0 
            if amount in dic:
                return dic[amount]
            temp = []
            for i in coins:
                if amount - i > -1:
                    te = rec(amount - i,dic)
                    if te == -1:
                        temp.append(float("inf"))
                    else:
                        temp.append(te+1)
                    dic[amount] = min(temp)
            print(temp,amount)
            if not temp:
                print("we are at -1",amount)
                return -1
            return min(temp)
        res = rec(amount,dic)
        if res == float("inf"):
            return -1
        return res
        print(dic)
        