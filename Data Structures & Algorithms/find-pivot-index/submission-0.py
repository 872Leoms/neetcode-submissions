class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        temp1 = [nums[0]]
        temp2 = [nums[len(nums)-1]]
        for i in range(1,len(nums)):
            k = nums[i] + temp1[i-1]
            temp1.append(k)
        for i in range(len(nums)-2,-1,-1):
            k = nums[i] + temp2[-1]
            temp2.append(k)
        temp2.reverse()
        temp2 = [0] + temp2 + [0] 
        temp1 = [0] + temp1 + [0]
        for i in range(len(nums)):
            if temp2[i+2] == temp1[i]:
                return i
        return -1
        print(temp1)
        print(temp2)


        