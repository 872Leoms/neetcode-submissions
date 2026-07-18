class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        pattrens=[]
        def rec(nums,ind,target,patt):
            if target == 0:
                pattrens.append(patt)
                return
            if target < 0:
                return
            for i in range(ind,len(nums)):
                rec(nums,i,target-nums[i],patt+[nums[i]])
        rec(nums,0,target,[])
        return(pattrens)
        