class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        even = (len(nums1) + len(nums2)) % 2 == 0
        total = len(nums1) + len(nums2)
        half = total // 2
        res = []
        p1,p2 = 0,0
        while len(res) <= half:
            if p1 < len(nums1) and p2 < len(nums2):
                value = nums1[p1] if nums1[p1] < nums2[p2] else nums2[p2]
                if nums1[p1] < nums2[p2]:p1+= 1 
                else: p2 += 1
            else:
                value = nums1[p1] if p1 < len(nums1) else nums2[p2]
                if p1 < len(nums1):p1 += 1
                else: p2 += 1
            res.append(value)
        if even:
           return (res[-1] + res[-2]) / 2
        else:
            return res[-1]


        