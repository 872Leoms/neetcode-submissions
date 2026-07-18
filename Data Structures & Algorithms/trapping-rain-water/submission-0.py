class Solution:
    def trap(self, height: List[int]) -> int:
        right= [height[0]] + ([0] * (len(height) - 1))
        left = ([0] * (len(height) - 1)) + [height[-1]]
        i,j = 1,len(height) - 2
        while i < len(height) and j > -1:
            if height[i] >= right[i - 1]:
                right[i] = height[i]
            else:
                right[i] = right[i-1]

            if height[j] >= left[j + 1]:
                left[j] = height[j]
            else:
                left[j] = left[j + 1]     
            i += 1
            j -= 1
        res = []
        for i in range(len(left)):
            thm = min(right[i],left[i]) - height[i]
            res.append(thm)
        print(left)  
        print(right)
        return(sum(res))