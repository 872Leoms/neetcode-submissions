class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        maxsub = 2 ** length
        res = []
        for i in range(maxsub):
            cursub = []
            for j in range(length):
                if i & (1 << j):
                    cursub.append(nums[j])
            res.append(cursub)
        return(res)

        