class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        pattrens=[]
        def rec(nums,ind,target,patt):
            if ind > len(nums):
                print(f"ind > len(nums){target}")
                return
            if target < 0:
                return
            if target == 0:
                print(f"target zero {target}")
                pattrens.append(patt)
            if target < nums[ind]:
                ind +=1
            for i in range(ind,len(nums)):
                rec(nums,i,target-nums[i],patt+[nums[i]])
        rec(nums,0,target,[])
        return(pattrens)
        