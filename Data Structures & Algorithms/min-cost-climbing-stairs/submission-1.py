class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic = {}
        thesmall = 0
        def rec(i,dic):
            if i == len(cost):
                print("in the len")
                return 0
            if i in dic:
                print("in the dic")
                return dic[i]
            temp1,temp2 = float("inf"),float('inf')
            if i + 1 <= len(cost):
                print("in the i+1",i)
                temp1 = rec(i + 1,dic) + cost[i]
            if i + 2 <= len(cost):
                print("in the i + 2")
                temp2 = rec(i + 2, dic) + cost[i]
            summ = min(temp1,temp2)
            print(summ,i)
            dic[i] = summ
            print(dic)
            return summ
        (rec(-1,dic))
        return(min(dic[0],dic[1]))
