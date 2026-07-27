class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        even = (len(nums1) + len(nums2)) % 2 == 0
        a,b = nums1,nums2
        if len(a) > len(b):
            a,b = b,a
        p1,p2 = 0,len(a) - 1
        half = (len(a) + len(b)) // 2
        while True:
            middle = (p1 + p2) // 2
            point = half - middle - 2
            lefta = a[middle] if middle >= 0 else float("-inf")
            righta = a[middle + 1] if (middle +1)< len(a) else float("inf")
            leftb = b[point ] if point >= 0 else float("-inf")
            rightb = b[point+1] if (point+1) < len(b) else float("inf")
            if lefta <= rightb and leftb <= righta:
                if even:
                    return(max(lefta,leftb) + min(righta,rightb)) / 2
                else:
                    return min(righta,rightb)
            if lefta > rightb:
                p2 = middle - 1
            else:
                p1 = middle + 1            

        