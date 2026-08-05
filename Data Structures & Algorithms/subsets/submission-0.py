class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(i,thelist):
            print(i)                
            res.append(thelist)
            for j in range(i,len(nums)):
                temp = thelist + [nums[j]]
                print(j)
                rec(j + 1,temp)
            return
        rec(0,[])
        return(res)
        