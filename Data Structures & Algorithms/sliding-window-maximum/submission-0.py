class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = 0
        set1 = list()
        res = []
        for i in range(len(nums)):
            if i != 0:
                set1.remove(nums[i-1])
            if len(nums) - i < k:
                break
            while d < i + k and d < len(nums):
                set1.append(nums[d])
                d+=1
            res.append(max(set1))
        return(res)


        