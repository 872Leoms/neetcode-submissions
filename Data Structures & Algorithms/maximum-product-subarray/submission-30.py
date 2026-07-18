class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg = nums[0]
        ans = nums[0]
        pos = nums[0]
        for i in range(1,len(nums)):
            current = nums[i]
            npos = current * pos
            nneg = current * neg
            neg = min(current,nneg,npos)
            pos = max(current,nneg,npos)
            ans = max(ans,pos)
        return ans


        