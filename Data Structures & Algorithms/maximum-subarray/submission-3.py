class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return nums[0] 
        i = 0
        j = 1
        summ = nums[i]
        maxx = summ
        while i < len(nums)  and j < len(nums):
            temp = summ
            if temp + nums[j] <= nums[j]:
                i = j
                summ = nums[j]
            else:
                summ += nums[j]
            maxx = max(summ,temp,maxx)
            print(f"the temp = {temp} | the sum = {summ} | the nums i = {nums[i]} | the nums j = {nums[j]} | the maxx ={maxx}")
            j += 1
        return(maxx)
