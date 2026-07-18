class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(per,arr):
            print(per)
            print(arr)
            if len(per) == len(arr):
                res.append(per)
                return
            else:
                for i in arr:
                    if i in per:
                        continue
                    else:
                        temp = per +[i]
                        rec(temp,arr)
        rec([],nums)
        return(res)

        