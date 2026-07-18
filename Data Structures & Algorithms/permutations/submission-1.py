class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(arr,ind):
            if ind == len(arr):
                res.append(arr[:])
                return
            for i in range(ind,len(arr)):
                    arr[i],arr[ind] = arr[ind],arr[i]
                    rec(arr,ind+1)
                    arr[i],arr[ind] = arr[ind],arr[i]
        rec(nums,0)
        return(res)