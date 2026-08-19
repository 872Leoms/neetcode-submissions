class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def rec(ind,summ,curr):
            if summ == target:
                res.append(curr.copy())
                return
            for i in range(ind,len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if summ + candidates[i] > target:
                    return           
                curr.append(candidates[i])
                rec(i + 1,summ + candidates[i],curr)
                curr.pop()               
        rec(0,0,[])
        return res
    
        