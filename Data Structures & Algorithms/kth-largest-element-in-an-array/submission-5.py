class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        k = len(nums) - k
        while True:
            left = start
            piot = start
            piotvalue = nums[start]
            for i in range(start + 1,end+ 1):
                if nums[i] <= piotvalue:
                    left += 1
                    nums[left],nums[i] = nums[i],nums[left]
            nums[start],nums[left] = nums[left],nums[start]
            if left == k:
                return nums[k]
            elif left < k:
                start = left + 1
            else:
                end = left - 1



