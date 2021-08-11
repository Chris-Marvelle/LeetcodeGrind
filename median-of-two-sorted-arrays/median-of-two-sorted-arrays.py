class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = nums1 + nums2
        s.sort()
        print(s)
        if len(s) % 2 == 0:
            x = len(s) // 2
            return (s[x] + s[x-1]) / 2
        else:
            print(len(s)//2)
            return s[len(s)//2]