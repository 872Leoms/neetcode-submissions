class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        for i in range(len(heights)):
            large = 1
            stack.append(large * heights[i])
            themul = heights[i]
            for j in range(len(heights)):
                if j == i:
                    continue
                else:
                    if heights[i] <= heights[j]:
                        large += 1
                    elif heights[i] > heights[j] and((j < i - 1) or j == i -1):
                        large = 1
                    elif heights[i] > heights[j] and (j < i):
                        large += 1
                        themul = heights[j]
                        break
                    elif heights[i] > heights[j]:
                        break
            stack.append((large) * themul)
        print(stack)

        return(max(stack))
        