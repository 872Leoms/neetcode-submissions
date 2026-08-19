class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        pattrens=[]
        nums.sort()
        def rec(ind,summ,patt):
            if target == summ:
                pattrens.append(patt.copy())
                return
            for i in range(ind,len(nums)):
                if summ + nums[i] > target:
                    return
                patt.append(nums[i])
                rec(i,summ + nums[i],patt)
                patt.pop()
        rec(0,0,[])
        return(pattrens)
        